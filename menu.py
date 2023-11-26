# Menu temporaire pour tester les fonctions
from main import *

numero = int(input("Saisir le numéro de la question (fonctionnalités à développer) : "))
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
    resultat = apparition_mot("./cleaned", "nation")
    print(resultat)

elif numero == 5:
    resultat = premier_a_parler("./cleaned", "climat")
    print(resultat)

elif numero == 6:
    resultat = mots_evoques("./cleaned")
    print(resultat)

else:
    print("Le numéro de l'exercice ne correspond pas")