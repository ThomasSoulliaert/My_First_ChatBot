# Menu temporaire pour tester les fonctions
from main import *

numero = int(input("Saisir le numéro de la fonction: "))
matrice = TF_IDF("./cleaned")

if numero == 1:
    liste = mots_non_importants(matrice)
    print(liste)

elif numero == 2:
    liste = mots_importants(matrice)
    print(liste)
