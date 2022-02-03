from math import *

        
print("Veuillez envoyer les valeurs suivantes: imc(masse(kg), taille(m))")
def imc(p, t):
    sortie= (p/t**2)
    print(sortie)
    if sortie < 18.5:
            return("Vous etes en sous-poids.")
    if sortie < 25:
            return("Votre poids est dans la normalite.")
    if sortie > 25:
            print("Vous etes en surpoids.")
    if sortie > 30:
        print("Vous etes en obesite.")

        
