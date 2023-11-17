# Projet Python - My first ChatBOT

# Partie 1
# 1.1 - Extraire les noms des présidents à partir des noms des fichiers texte fournis
import os
import re
import string


def extraire_noms_presidents(dossier):
    # code Python utilisé pour parcourir la liste des fichiers d’une extension donnée et dans un répertoire donné
    noms_presidents = []

    # Parcourez chaque fichier dans le dossier
    for discours in os.listdir(dossier):
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
        if nom[:-1] not in noms_presidents_sans_doublons and nom[-1] in [str(i) for i in range(10)]:
            noms_presidents_sans_doublons.append(nom[:-1])

        elif nom not in noms_presidents_sans_doublons and nom[-1] not in [str(i) for i in range(10)]:
            noms_presidents_sans_doublons.append(nom)

    return noms_presidents_sans_doublons


liste_noms_presidents = liste_sans_doublons(liste_noms_presidents_originale)


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

    # Retourner le dictionnaire
    return dictionnaire


# Appel de la fonction pour créer le dictionnaire
dico_noms_prenoms_presidents = attribution_prenom(liste_noms_presidents)

# 1.3 - Afficher la liste des noms des présidents (sans doublons)
print(liste_noms_presidents)


# Afficher le dictionnaire des noms / prénoms des présidents
for president in dico_noms_prenoms_presidents.items():
    print(president)


# 1.4 - Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers.
def convertir_minuscule(dossier_source, dossier_destination):
    # Créer le nouveau dossier s'il n'existe pas déjà
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    # Parcours de chaque fichier du dossier source
    for file_name in os.listdir(dossier_source):
        # Chemin complet pour le fichier source et destination
        source_file_path = os.path.join(dossier_source, file_name)
        destination_file_path = os.path.join(dossier_destination, file_name)

        # Vérifie que le fichier est un fichier texte
        if file_name.endswith(".txt"):
            # Ouvre le fichier source en lecture
            with open(source_file_path, 'r') as source_file:
                # Lit le contenu du fichier et le convertit en minuscules
                content = source_file.read().lower()

                # Crée un nouveau fichier dans le dossier destination avec le contenu en minuscules
                with open(destination_file_path, 'w', encoding='utf-8') as destination_file:
                    destination_file.write(content)


# Appel de la fonction
convertir_minuscule("speeches", "cleaned")


# 1.5 - Parcourir chaque texte du cleaned et supprimer tout caractère de ponctuation (sauf ' et - à remplacer par un espace)
def supprimer_ponctuation(dossier):
    # Parcours de chaque fichier du dossier source
    for file_name in os.listdir(dossier):

        # Chemin complet pour le fichier source
        source_file_path = os.path.join(dossier, file_name)

        # Vérifie que le fichier est un fichier texte
        if file_name.endswith(".txt"):
            # Ouvre le fichier source en lecture
            with open(source_file_path, 'r') as source_file:
                # Lit le contenu du fichier
                contenu = source_file.read()

                # Crée une fonction pour remplacer la ponctuation et les tirets par des espaces
                def nettoyer_texte(text):
                    for c in text:
                        if (c == "'" or c == '-') :
                            cleaned_text = ''.join(' ')
                        elif c in string.punctuation:
                            cleaned_text = ''.join('')
                        else:
                            cleaned_text = ''.join(c)



                    #cleaned_text = ''.join(' ' if (c =="'" or c == '-') ''elif c in string.punctuation else c for c in text)
                    return cleaned_text

                # Nettoie le contenu du fichier
                nouveau_contenu = nettoyer_texte(contenu)

            # Réécrire le fichier avec le contenu nettoyé
            with open(source_file_path, 'w', encoding='utf-8') as source_file:
                source_file.write(nouveau_contenu)


# Appel de la fonction
supprimer_ponctuation("cleaned")



