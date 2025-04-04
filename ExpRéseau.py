 #* Simulation du trafic réseau
 #* Simulation d'intervalle temporelle d'acceptation de 2 paquets successifs dans un réseau avec la loi exponentielle
 
import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import *

#! Loi Exponentielle | Méthode de rejet

def rejet(f,g,c): # On prend f la densité de la v.a. à simuler,
                  # g la densité de la v.a. qu'on peut déja simuler -dans notre cas c'est l'uniforme entre 0 et 1-,
                  # et c une constante prédétérminée 
    while True:
        x = random()
        u = random()
        # print(exp(-duree*lambda_paquets*x))
        # print("x: ",x)
        # print("u: ",u)
        # print("Rapport: ",f(x)/(c*g(x)))
        if u < f(x)/(c*g(x)):
            return x

lambda_paquets = 60  #! Paquets par seconde
duree = 2 #! Durée d'acceptation de paquets (secondes)

attente_max = 50  #! temps d'attente maximal (millisecondes)

temps_entre_2paquets = np.zeros([lambda_paquets*duree - 1])
for i in range(len(temps_entre_2paquets)):
    temps_entre_2paquets[i] = round((rejet(lambda x: lambda_paquets*exp(-lambda_paquets*x),lambda x: 1,lambda_paquets)) * 1000) # On multiplie par 1000 pour avoir des millisecondes
    # temps_entre_2paquets[i] = np.random.exponential(duree*lambda_paquets)
# print(temps_entre_2paquets)

congestion = temps_entre_2paquets > attente_max
pourcentage_congestion = np.mean(congestion) * 100

print(f"Pourcentage de congestion : {pourcentage_congestion:.2f}%")

plt.plot(temps_entre_2paquets, marker='o')
plt.axhline(y=attente_max, color='red', linestyle='--', label="Temps d'attente max")
plt.title("Simulation du Trafic Réseau: Temps d'attente entre 2 Paquets")
plt.xlabel("Couples de Paquets successifs")
plt.ylabel("Temps d'attente (ms)")
plt.legend()
plt.show()