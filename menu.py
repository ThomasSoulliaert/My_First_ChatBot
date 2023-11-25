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

elif numero == 3:
    liste1 = mots_repetes("./Nomination_Chirac1.txt")
    liste2 = mots_repetes("./Nomination_Chirac1.txt")
    liste3 = liste1
    for mot in liste2:
        if mot not in liste3:
            liste3.append(mot)
    print(liste3)

elif numero == 4:
    liste = apparition_mot()