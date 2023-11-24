# Projet Python - My first ChatBOT
# Testy
import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Partie 1
# 1.1 - Extraire les noms des présidents à partir des noms des fichiers texte fournis
def extraire_noms_presidents(dossier):
    # code Python utilisé pour parcourir la liste des fichiers d’une extension donnée et dans un répertoire donné
    noms_presidents = []

    # Parcourez chaque fichier dans le dossier
    for discours in os.listdir(dossier):
        if discours.endswith(".txt"):
            nom_president = discours.split("_")[1].split(".")[0]
            noms_presidents.append(nom_president)

    return noms_presidents

# Appel de la fonction
liste_noms_presidents = extraire_noms_presidents("speeches")

# Changer la liste principale pour éviter les doublons
def liste_sans_doublons(liste):
    L = []
    
    # Utilisation des slices pour éviter les doublons
    for nom in liste:
        if nom[:-1] not in L and nom[-1] in [str(i) for i in range (10)]:
            L.append(nom[:-1])
            
        elif nom not in L and nom[-1] not in [str(i) for i in range (10)]:
            L.append(nom)
            
    return L

# Appel de la fonction
liste_noms_presidents_sans_doublons = liste_sans_doublons(liste_noms_presidents)


# 1.2 - Associer à chaque président un prénom
def attribution_prenom(liste):
    # Création d'un dictionnnaire pour associer à chaque nom un prénom
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
    
    return dictionnaire

# Appel de la fonction
dico_noms_prenoms_presidents = attribution_prenom(liste_noms_presidents_sans_doublons)


# 1.3 - Afficher la liste des noms des présidents (sans doublons)
print(liste_noms_presidents)


# 1.4 - Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers. 

def convertir_minuscules(dossier_entree, dossier_sortie):
    # Créer un dossier de sortie s'il n'existe pas
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    # Liste des fichiers texte dans le dossier d'entrée
    fichiers = list_of_files(dossier_entree, ".txt")

    # Conversion des fichiers texte en minuscules et sauvegarde dans le dossier de sortie
    for fichier in fichiers:
        with open(os.path.join(dossier_entree, fichier), 'r') as file:
            contenu = file.read().lower()

        with open(os.path.join(dossier_sortie, fichier), 'w') as file_out:
            file_out.write(contenu)

# Appel de la fonction
convertir_minuscules("./speeches", "./cleaned")


def supprimer_ponctuation(dossier):
    # Liste des fichiers texte dans le dossier
    file_list = list_of_files(dossier, ".txt")

    # Suppression des virgules dans les fichiers texte
    for fichier in file_list:
        with open(os.path.join(dossier, fichier), 'r') as file:

            contenu = file.read()

            nouveau_contenu = ''
            for c in contenu:
                if c == "'" or c == '-':
                    nouveau_contenu += ' '  # Remplacer par un espace
                elif c not in ['.', ',', ':', '!', '?', ';', '/', '«', '»', '*', '_']:
                    nouveau_contenu += c  # Ajouter le caractère s'il n'est pas une ponctuation

        with open(os.path.join(dossier, fichier), 'w') as file_out:
            file_out.write(nouveau_contenu)

# Appel de la fonction avec le dossier "cleaned"
supprimer_ponctuation("./cleaned")


# II - La méthode TF-IDF
# 2.1 - Associer à chaque mot le nombre de fois qu’il apparait dans la chaîne de caractères
def TF(fichier):
    # Création d'un dictionnnaire pour associer à chaque mot un nombre d'occurrence
    with open(f"./cleaned/{fichier}", "r") as f:
        liste_mots = f.read().split()

        dictionnaire = {}

        for mot in liste_mots:
            if mot in dictionnaire:
                dictionnaire[mot] += 1
            else:
                dictionnaire[mot] = 1

        return dictionnaire
            
# Appel de la fonction
x = TF("Nomination_Macron.txt")


# 2.2 - Dictionnaire associant à chaque mot son score IDF
def IDF(dossier):
    file_list = list_of_files(dossier, ".txt")

    dictionnaire = {}

    for fichier in file_list:
        nombre_mots = TF(fichier)
        for i in nombre_mots:
            if i in dictionnaire:
                dictionnaire[i] += 1
            else:
                dictionnaire[i] = 1

    for key, val in dictionnaire.items():
        dictionnaire[key] = math.log(len(file_list) / val)

    return dictionnaire

# Appel de la fonction
score_IDF = IDF("./cleaned")
print(score_IDF)