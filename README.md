# pychatbot-biville-lefrancq-soulliaert-d

EFREI Paris, L1, Groupe D

Noms des membre de l’équipe projet:
- BIVILLE Guillaume
- LEFRANCQ Nicolas
- SOULLIAERT Thomas

Noms des professeurs:
- CHABCHOUB Kamel
- YAHIAOUI Itheri

Fonctionnalités principales : 

Partie I

# 1.1 - Extraire les noms des présidents à partir des noms des fichiers texte fournis

Pour la première fonction, nous avons extrait les noms des présidents à partir des noms des fichiers texte fournis. La fonction s’appelle “extraire_noms_presidents” et prend en paramètre un dossier. Nous avons initialisé une liste “noms_presidents”, puis nous parcourons chaque discours dans le dossier “spechees”. Si le type du fichier se termine par “.txt”, alors nous utilisons les “split” pour délimiter la partie du titre du fichier qui nous intéresse. Le [1] sert à prendre la partie après le caractère indiqué (ici, “_”) et le [0] sert à prendre la partie avant le caractère indiqué (ici, le “.”). Enfin, nous ajoutons ce que nous venons de délimiter à la liste “noms_presidents” et nous renvoyons la liste. 


# 1.2 - Associer à chaque président un prénom

Pour la deuxième fonction, nous associons à chaque président un prénom. La fonction s’appelle “attribution_prenom” et prend en paramètre une liste. Pour cela nous initialisons un dictionnaire, qui à chaque clé (nom) va associer une valeur (prénom) en parcourant chaque nom dans la liste. Ensuite, nous utilisons des “if” et “elif” pour l’attribution des prénoms en fonction des noms. Enfin, nous renvoyons le dictionnaire.

Pour la troisième fonction, nous devons afficher la liste des noms des présidents (sans doublons). La fonction s’appelle “liste_sans_doublons” et prend en paramètre une liste. Pour cela nous initialisons une liste “L”. Ensuite nous parcourons dans la liste en paramètre chaque élément. Avec des “slices”, nous cherchons à savoir s’il existe plusieurs discours (éléments se terminant par un chiffre). Si c’est le cas, on enlève le dernier caractère de cet élément avec [:-1] et si cet élément n’est pas dans la liste “L” et que son dernier caractère est un chiffre, on l’ajoute. Sinon, si l’élément n’est pas dans la nouvelle liste et que son dernier caractère n’est pas un chiffre (cas ou il n’y a pas de doublons), on l’ajoute à la liste “L”. Enfin nous renvoyons la liste “L”.


# 1.3 - Afficher la liste des noms des présidents (sans doublons)


# 1.4 - Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers.

La fonction "convertir_minuscules" a pour objectif de convertir le contenu de fichiers texte présents dans un dossier d'entrée en minuscules, puis de stocker ces contenus dans de nouveaux fichiers dans un dossier de sortie.
On crée le dossier de sortie. On vérifie si le dossier de sortie spécifié existe. Si non, il est créé. 

On utilise la fonction "list_of_files" pour obtenir la liste des fichiers texte dans le dossier d'entrée avec l'extension ".txt". Puis on convertit les fichiers en minuscules : Pour chaque fichier, on ouvre le fichier en lecture ('r'), on lit son contenu, on le convertit en minuscules à l'aide de "lower()", puis on  stocke le contenu converti. 
Enfin on sauvegarde dans le dossier de sortie :  Ouvre un nouveau fichier dans le dossier de sortie en écriture ('w') et on  y écrit le contenu converti en minuscules.

Pour la fonction "supprimer_ponctuation", l'objectif est de supprimer certains caractères de ponctuation spécifiques des fichiers texte dans un dossier. On  utilise la fonction "list_of_files"" pour obtenir la liste des fichiers texte dans le dossier spécifié. Ensuite pour chaque fichier, on ouvre le fichier en lecture ('r'), on lit son contenu et on crée un nouveau contenu en remplaçant certains caractères de ponctuation spécifiques par des espaces, et en conservant les autres caractères. Puis on écrit le nouveau contenu dans le même fichier.


# II - La méthode TF-IDF
# 2.1 - Associer à chaque mot le nombre de fois qu’il apparait dans la chaîne de caractères

La fonction TF a pour objectif d'associer à chaque mot le nombre de fois qu'il apparaît dans une chaîne de caractères provenant d'un fichier texte. La fonction prend en paramètre le nom du fichier (fichier) à partir duquel elle va extraire le texte. Elle ouvre le fichier, lit son contenu, et divise le texte en une liste de mots. En utilisant un dictionnaire (dictionnaire), elle parcourt la liste de mots et compte le nombre d'occurrences de chaque mot. Si le mot est déjà présent dans le dictionnaire, son compteur est incrémenté. Sinon, une nouvelle entrée est créée avec le compteur initialisé à 1. à la fin , la fonction retourne le dictionnaire résultant qui associe chaque mot à son nombre d'occurrences dans le fichier.


# 2.2 - Dictionnaire associant à chaque mot son score IDF

La fonction IDF vise à créer un dictionnaire associant à chaque mot son score IDF basé sur l'ensemble des fichiers présents dans un dossier. La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels le calcul IDf sera effectué. Elle utilise la fonction  TF pour obtenir la fréquence d'apparition de chaque mot dans chaque fichier du dossier. Elle utilise un dictionnaire (dictionnaire) pour compter le nombre de fichiers dans lesquels chaque mot apparaît. Elle calcule le score IDF pour chaque mot en utilisant la formule mathématique IDF = log(N / n), où N est le nombre total de fichiers et n est le nombre de fichiers contenant le mot. ET la fonction retourne le dictionnaire associant chaque mot à son score IDF. Cette fonction est utilisée pour obtenir le score IDF de chaque mot, qui sera ensuite utilisé dans le calcul du score TF-IDF. 
Enfin, l'appel "score_IDF = IDF("./cleaned")" génère le dictionnaire associant à chaque mot son score IDF pour l'ensemble des fichiers du dossier "cleaned".

En résumé, le programme calcule d'abord la fréquence d'apparition de chaque mot dans chaque fichier (TF), puis utilise ces informations pour calculer le score IDF de chaque mot sur l'ensemble des fichierrs (IDF).


# 2.3 - Méthode TF-IDF

La fonction "TF_IDF" vise à calculer la matrice TF-IDF pour chaque mot dans chaque fichier d'un dossier. La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels le calcul TF-IDF sera effectué. Elle utilise la fonction ""list_of_files" pour obtenir la liste des fichiers du dossier et la fonction IDF pour obtenir le score IDF de chaque mot. Elle initialise une matrice vide (matrice) qui stockera les valeurs TF-IDF pour chaque mot dans chaque fichier. Elle parcourt chaque mot présent dans le score IDF (obtenu à partir de la fonction IDF). Pour chaque mot, elle crée une liste qui commence par ce mot et ensuite ajoute les valeurs TF-IDF pour ce mot dans chaque fichier du dossier, (la valeur TF-IDF pour un mot dans un fichier est calculée en multipliant le score TF obtenu à partir de la fonction TF et le score IDF obtenu précédemment. Si le mot n'est pas présent dans le fichier, elle ajoute 0 à la liste. La liste est ensuite ajoutée à la matrice. La fonction retourne la matrice résultante qui contient les valeurs TF-IDF pour chaque mot dans chaque fichier.

L'appel "matrice = TF_IDF("./cleaned")" génère la matrice TF-IDF pour tous les mots dans tous les fichiers du dossier "cleaned".


# III - Fonctionnalités à développer
# 3.1 - Afficher la liste des mots les moins importants dans le corpus de documents (TD-IDF = 0 dans tous les fichiers)

La fonction "mots_non_importants" a pour objectif d'afficher la liste des mots les moins importants dans le corpus de documents, c'est-à-dire ceux ayant un score TF-IDF égal à 0 dans tous les fichiers. POur le faire la fonction prend en paramètre la matrice TF-IDF (matrice) générée précédemment. Elle répète sur chaque ligne de la matrice, représentant un mot. Pour chaque mot, elle calcule la somme de ses scores TF-IDF dans tous les fichiers. Et si la somme est égale à 0, cela signifie que le mot a un score TF-IDF nul dans tous les fichiers, et il est ajouté à la liste des mots non importants.


# 3.2 - Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé

La fonction "mots_importants" a pour objectif d'afficher les mots ayant le score TF-IDF le plus élevé parmi tous les fichiers. La fonction prend en paramètre la matrice TF-IDF (matrice) générée précédemment. Elle répète sur chaque ligne de la matrice, représentant un mot. Elle recherche le score TF-IDF le plus élevé parmi tous les fichiers. Et pour finir, elle identifie les mots ayant ce score et les ajoute à la liste des mots importants.


# 3.3 - Indiquer le(s) mot(s) le(s) plus répété(s) par un président (dans le test, Chirac)

La fonction "mots_repetes" a pour objectif d'indiquer les mots les plus répétés par un président donné. La fonction prend en paramètre le nom du fichier (fichier) correspondant au discours d'un président. Elle utilise la fonction TF pour obtenir le nombre d'occurrences de chaque mot dans le fichier. Elle identifie le score le plus élevé parmi les occurrences de chaque mot. 
Et ensuite, elle ajoute à la liste tous les mots ayant ce score.


# 3.4 - Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois

La fonction "apparition_mot" a pour objectif d'indiquer les noms des présidents qui a ontt parlé de la "Nation" et celui qui l’a répété le plus de fois. Ainsi la fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche sera effectuée et le mot à rechercher (mot_recherche). Elle utilise la fonction "list_of_files" pour obtenir la liste des fichiers du dossier. Elle utilise la fonction "extraire_noms_presidents" pour obtenir la liste des noms des présidents à partir des noms de fichiers. Elle initialise un dictionnaire vide (dictionnaire) qui stockera le nombre d'occurrences du mot recherché par président. Elle parcourt chaque fichier du dossier et et ensuite utilise la fonction TF pour obtenir le nombre d'occurrences du mot recherché, et stocke ces informations dans le dictionnaire pour enfin identifié la liste des présidents qui ont parlé du mot. Elle détermine le président qui a répeté le mot le plus de fois en comparant les occurrences dans le dictionnaire.


# 3.5 - Indiquer le premier président à parler du climat et/ou de l’écologie

La fonction premier_a_parler a pour objectif d'indiquer le premier président à parler du climat ou de de l’écologie. La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche sera effectuée et le mot à rechercher (mot_recherche). Elle utilise la fonction "list_of_files" pour obtenir la liste des fichiers du dossier. Elle initialise un dictionnaire vide (dictionnaire) qui stockera l'indice de la première occurrence du mot recherché par président. Elle parcourt chaque fichier du dossier, utilise la fonction TF pour obtenir le nombre d'occurrences du mot recherché, et stocke l'indice de la première occurrence dans le dictionnaire.  Et enfin ellle identifie le président qui a mentionné le mot en premier en comparant les indices dans le dictionnaire.


# 3.6 - Hormis les mots dits « non importants », liste de(s) mot(s) que tous les présidents ont évoqués

L'objectif de la fonction "mots_evoques" est de lister les mots que tous les présidents ont évoqués, sauf les mots "non importants" (ceux avec un score TF-IDF de 0 dans tous les fichiers). La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche se base. Elle utilise la fonction  "list_of_files" pour obtenir la liste des fichiers du dossier. Elle utilise la fonction TF pour obtenir la fréquence d'apparition de chaque mot dans le premier fichier de la liste (file_list[0]), qui sert de référence. Elle initialise une liste vide (liste) qui stockera les mots évoqués par par tous les présidents. Elle parcourt chaque mot dans le dictionnaire de fréquence de référence. 
Pour chaque mot, elle vérifie s'il est présent dans la fréquence d'apparition de chaque président (dans chaque fichier du dossier). Si le mot est présent dans tous les fichiers, elle l'ajoute à la liste des mots évoqués par tous les présidents et retourne la liste.




Partie II

# 1 - Tokenisation de la question


La fonction "transformer_en_liste_de_mots_une_chaine" a pour onjectif principal de prendre une chaîine de caractères en entrée et de renvoyer une liste contenant tous les mots présents dasns cette cahîne.

Dans cette fonction, on initialise d'abord une liste vide "liste = []".
Cette liste va contenir les mots extraits de la chaîne, et une chaîne de caractères vide (mot) qui servira à construire les mots au fur et à mesure du parocurs de la chaîne;
La fonction parcourt chaque caractère de la chaîne d'entrée à l'aide de la boucle 'for'.

On vérifie ensuite si le caractère est alphabétique (s'il se situe entre 'a' et 'z' ou 'A' et 'Z') à l'aide de 'isalpha'. Si le caractère est alphabétique, il est ajouté à la fin du mot en cours de contsruction (mot) et tous les caractères alphabétiques sont convertis en minuscule avec 'lower'. Puis on retounrne la liste à la fin.


# 2 - Recherche de mots de la question dans le Corpus

La fonction "recherche_mots_corpus" commence par appeler de la fonction "transformer_en_liste_de_mots_une_chaine(question)", qui transforme la chaine de caractères de la question en une liste de mots.
Ensuite la fonction crée une matrice TF IDF à partir du corpus en appelant la focntion TF_IDF(dossier).
La fonction parcourt chaque mot de la liste obtenue à partir de la question (liste) et parcourt ensuite chque ligne de la matrice TF-IDF. Si le mot est préent dans une ligne d ela matrice, il est ajouté à la liste liste_mots_du_corpus.
La fonction retourne la liste liste_mots_du_corpus qui contient le smots de la question qui sont présent.

# 3 - Calcul de vecteur TF-IDF pour les termes de la question

La fonction "TF_IDF_2" commence par obtenir une liste de fichiers texte présents dans le dossier spéifié en appelant la fonction list_of_files(dossier, ".txt"). 








