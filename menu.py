# Menu temporaire de la partie 1 pour tester les fonctions
from main import *

choix = int(input("Tapez 1 pour les fonctionnalités de la Partie 1 OU tapez 2 pour ChatBOT : "))

if choix == 1:
    numero = int(input("Saisir le numéro de la question : "))
    matrice_test = TF_IDF_Test("./cleaned")

    if numero == 1:
        liste = mots_non_importants(matrice_test)
        print(liste)

    elif numero == 2:
        liste = mots_importants(matrice_test)
        print(liste)

    elif numero == 3:
        liste1 = mots_repetes("./Nomination_Chirac1.txt", "./cleaned")
        liste2 = mots_repetes("./Nomination_Chirac2.txt", "./cleaned")
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
        print("Le numéro de l'exercice ne correspond pas.")

elif choix == 2:
    question = input("Posez votre question : ")
    reponse = affinage_reponse(question, "./cleaned","./speeches")
    print(reponse)

else:
    print("Le numéro sélectionné n'existe pas.")