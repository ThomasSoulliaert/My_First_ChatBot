# Projet Python - My first ChatBOT

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
    nouvelle_liste = []
    
    # Utilisation des slices pour éviter les doublons
    for nom in liste:
        if nom[:-1] not in nouvelle_liste and nom[-1] in [str(i) for i in range (10)]:
            nouvelle_liste.append(nom[:-1])
            
        elif nom not in nouvelle_liste and nom[-1] not in [str(i) for i in range (10)]:
            nouvelle_liste.append(nom)
            
    return nouvelle_liste

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
dictionnaire_noms_prenoms_presidents = attribution_prenom(liste_noms_presidents_sans_doublons)


# 1.3 - Afficher la liste des noms des présidents (sans doublons)
print("La liste des présidents est : ", liste_noms_presidents_sans_doublons)


# 1.4 - Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers.
def convertir_minuscules(dossier_entree, dossier_sortie):
    # Créer un dossier de sortie s'il n'existe pas
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    # Liste des fichiers texte dans le dossier d'entrée
    file_list = list_of_files(dossier_entree, ".txt")

    # Conversion des fichiers texte en minuscules et sauvegarde dans le dossier de sortie
    for fichier in file_list:
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

# Appel de la fonction
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


# 2.3 - Méthode TF-IDF
def TF_IDF(dossier):
    file_list = list_of_files(dossier, ".txt")
    idf = IDF(dossier)

    matrice = []
    for mot in idf:
        liste = [mot]
        for fichier in file_list:
            tf = TF(fichier)

            if mot in tf:
                tf_idf = tf[mot] * idf[mot]
                liste.append(tf_idf)
            else:
                liste.append(0)

        matrice.append(liste)

    return matrice

# Appel de la fonction
matrice = TF_IDF("./cleaned")
#print(matrice)


# III - Fonctionnalités à développer
# 3.1 - Afficher la liste des mots les moins importants dans le corpus de documents (TD-IDF = 0 dans tous les fichiers)
def mots_non_importants(matrice):
    liste = []
    for i in range(len(matrice)):
        somme = 0
        for j in range(1, len(matrice[i])):
            somme += matrice[i][j]
        if somme == 0:
            liste.append(matrice[i][0])
    return liste


# 3.2 - Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé
def mots_importants(matrice):
    score = 0
    for i in range(len(matrice)):
        somme = 0
        for j in range(1, len(matrice[i])):
            if matrice[i][j] > score:
                score = matrice[i][j]

    liste = []
    for i in range(len(matrice)):
        ajouter_mot = False
        for j in range(1, len(matrice[i])):
            if matrice[i][j] == score:
                ajouter_mot = True
        if ajouter_mot == True:
            liste.append(matrice[i][0])

    return liste


# 3.3 - Indiquer le(s) mot(s) le(s) plus répété(s) par un président (dans le test, Chirac)
def mots_repetes(fichier):
    tf = TF(fichier)
    score = 0
    for occurrences in tf.values():
        if occurrences > score:
            score = occurrences

    liste = []
    for mot in tf.keys():
        if tf[mot] == score:
            liste.append(mot)

    return liste


# 3.4 - Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
def apparition_mot(dossier, mot_recherche):
    file_list = list_of_files(dossier, ".txt")
    L_noms_presidents = extraire_noms_presidents(dossier)
    dictionnaire = {}
    liste = []

    for fichier in file_list:
        tf = TF(fichier)
        if mot_recherche in tf.keys():
            nom_president = fichier.split("_")[1].split(".")[0]
            dictionnaire[nom_president] = tf[mot_recherche]

    for president in dictionnaire.keys():
        liste.append(president)
    liste_president = liste_sans_doublons(liste)

    score = 0
    president = ""
    for occurrences in dictionnaire.values():
        if occurrences > score:
            score = occurrences
    for cle, val in dictionnaire.items():
        if val == score:
            president = cle

    return (f"La liste des président à parler de {mot_recherche} est : {liste_president}",
            f"Le président qui a utilisé ce mot le plus de fois est : {president}")


# 3.5 - Indiquer le premier président à parler du climat et/ou de l’écologie
def premier_a_parler(dossier, mot_recherche):
    file_list = list_of_files(dossier, ".txt")
    dictionnaire = {}

    for fichier in file_list:
        tf = TF(fichier)
        if mot_recherche in tf.keys():
            cles = list(tf.keys())
            indice_cle = cles.index(mot_recherche)

            nom_president = fichier.split("_")[1].split(".")[0]
            dictionnaire[nom_president] = indice_cle

    indice_min = next(iter(dictionnaire.values()), None)
    president = ""
    for indice in dictionnaire.values():
        if indice < indice_min:
            indice_min = indice
    for cle, val in dictionnaire.items():
        if val == indice_min:
            president = cle

    return f"Le premier président à parler de {mot_recherche} est {president} à l'indice {indice_min}"


# 3.6 - Hormis les mots dits « non importants », liste de(s) mot(s) que tous les présidents ont évoqués
def mots_evoques(dossier):
    file_list = list_of_files(dossier, ".txt")
    tf_reference = TF(file_list[0])
    liste = []

    for mot in tf_reference.keys():
        score = 0
        for fichier in file_list:
            tf = TF(fichier)
            if mot in tf.keys():
                score += 1
        if score == len(file_list):
            liste.append(mot)

    return f"La liste des mots évoqués par tous les présidents est : {liste}"

