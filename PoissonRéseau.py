 #* Simulation du trafic réseau
 #* Simulation du nbre de paquets par seconde dans un réseau avec la loi de Poisson 

import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import *

#! Loi de Poisson | Méthode d'inversion (Cas Discret)
def poisson(l):
    lp = []
    k = 0
    p = exp(-l)*(l**k)/factorial(k)
    
    lc = [p]
    while lc[-1] < 0.99999:
        lp.append(p)
        k += 1
        p *= l/k
        lc.append(lc[-1] + p)
        
    u = random()
    for k in range(len(lc)):
        if u < lc[k]:
            return k
       

lambda_paquets = 100  #! Paquets par seconde
duree = 120  #! Durée d'acceptation de paquets (secondes)

cap_max = 115  #! Capacité maximale du réseau (paquets/seconde)

# paquets_par_seconde = np.random.poisson(lam=lambda_paquets, size=duree)
paquets_par_seconde = np.zeros([duree])
for i in range(duree):
    paquets_par_seconde[i] = (poisson(lambda_paquets))

congestion = paquets_par_seconde > cap_max
pourcentage_congestion = np.mean(congestion) * 100

print(f"Pourcentage de congestion : {pourcentage_congestion:.2f}%")

# print(type(congestion))
# print(congestion)

plt.plot(paquets_par_seconde, marker='o')
plt.axhline(y=cap_max, color='red', linestyle='--', label='Capacité max')
plt.title("Simulation du Trafic Réseau: Paquets/S")
plt.xlabel("Temps (secondes)")
plt.ylabel("Paquets reçus")
plt.legend()
plt.show()
