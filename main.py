# Projet Python - My first ChatBOT
dsdsdqsq
# Partie 1
# 1.1 - Extraire les noms des présidents à partir des noms des fichiers texte fournis
import os

def extraire_noms_presidents(dossier):
    fichiers = os.listdir(dossier)
    noms_presidents = []

    for discours in fichiers:
        if discours.endswith(".txt"):
            nom_president = discours.split("_")[1].split(".")[0]
            noms_presidents.append(nom_president)

    return noms_presidents

liste_noms_presidents_originale = extraire_noms_presidents("speeches")

# Changer la liste principale pour éviter les doublons
def liste_sans_doublons(liste):
    noms_presidents_sans_doublons = []
    
    # Utilisation des splits et des slices pour éviter les doublons
    for nom in liste:
        if nom[:-1] not in noms_presidents_sans_doublons and nom[-1] in [str(i) for i in range (10)]:
            noms_presidents_sans_doublons.append(nom[:-1])
            
        elif nom not in noms_presidents_sans_doublons and nom[-1] not in [str(i) for i in range (10)]:
            noms_presidents_sans_doublons.append(nom)
            
    return noms_presidents_sans_doublons

liste_noms_presidents = liste_sans_doublons(liste_noms_presidents_originale)


# 1.2 - Associer à chaque président un prénom
# Création d'un dictionnnaire pour associer à chaque nom un prénom
def attribution_prenom(liste):
    dictionnaire = {}

    # Parcourez chaque nom dans la liste
    for nom in liste:
        # Associez le nom à un prénom
        if nom == "Chirac":
            dictionnaire[nom] = "Jacques"
            
        elif nom == "Giscard dEstaing":
            dictionnaire[nom] = "Valéry"
            
        elif nom == "Hollande" or nom == "Mitterrand":
            dictionnaire[nom] = "François"
            
        elif nom == "Macron":
            dictionnaire[nom] = "Emmanuel"
            
        elif nom == "Sarkozy":
            dictionnaire[nom] = "Nicolas"
    
    # Retourner le dictionnaire
    return dictionnaire

# Appel de la fonction pour créer le dictionnaire
dico_noms_prenoms_presidents = attribution_prenom(liste_noms_presidents)


# 1.3 - Afficher la liste des noms des présidents (sans doublons)
print(liste_noms_presidents)

# Afficher le dictionnaire des noms / prénoms des présidents
# for president in dico_noms_prenoms_presidents.items():
    # print(president)
