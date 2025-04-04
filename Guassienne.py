 #* Simualtion d'une action financière
 #* Simulation du comportement(Prix et rendement) d'une action financière avec la loi normale

from math import *
from random import random
import numpy as np
import matplotlib.pyplot as plt

#! Loi Normale | Méthode Polaire
def normale(m,s):
    # r = np.random.exponential(1/2)
    u1 = random()
    u2 = random()
    return (sqrt(-2 * log(u1)) * cos(2 * pi * u2) * sqrt(s) + m)
    # return (sqrt(r) * cos(2 * pi * u1) * s + m)

prix_initial = 100
mu = 0.0005  #! Rendement moyen
sigma = 0.002 #! Volatilité
jours = 100  #! Nombre de jours
currency = "$"

rendements = np.zeros([jours])
for i in range(jours):
    rendements[i] = normale(mu, sigma)
# print(rendements)

#! Visualisation des rendements simulés
plt.subplot(2,1,1)
plt.plot(rendements, color='royalblue', marker='.')
plt.title("Simulation du comportement d'un rendement d'une action")
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Jours")
plt.ylabel("Rendements")
plt.grid(True)

# prix = prix_initial * np.cumprod(1 + rendements)
prix = np.zeros([jours])
prix[0] = prix_initial
for i in range(1, jours):
    prix[i] = prix[i-1] * (1 + rendements[i])

print(f"Prix final simulé : {prix[-1]:.2f} " + currency)
print(f"Profit final simulé : {prix[-1]-prix[0]:.2f} " + currency)

#! Visualisation de l'évolution du prix
plt.subplot(2,1,2)
plt.plot(prix, color='royalblue')
plt.title("Simulation de l'évolution du prix d'une action financière")
plt.axhline(y=prix_initial, color='red', linestyle='--', label='Prix initial')
plt.xlabel("Jours")
plt.ylabel("Prix de l'action (" + currency + ")")
plt.grid(True)

plt.suptitle("Simulation d'une action financière", fontsize=16, font='Times New Roman', fontweight='bold')
plt.tight_layout()
plt.legend()
plt.show()