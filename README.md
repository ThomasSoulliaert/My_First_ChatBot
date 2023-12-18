# pychatbot-biville-lefrancq-soulliaert-d

EFREI Paris, L1, Groupe D, Groupe 5 :

Noms des membre de l’équipe projet:
- BIVILLE Guillaume
- LEFRANCQ Nicolas
- SOULLIAERT Thomas

Noms des professeurs:
- CHABCHOUB Kamel
- YAHIAOUI Itheri


# Fichier main.py
# Fonctionnalités principales : 
# Partie I

# 1.1 - Extraire les noms des présidents à partir des noms des fichiers texte fournis
Pour la première fonction, nous avons extrait les noms des présidents à partir des noms des fichiers texte fournis. La fonction s’appelle “extraire_noms_presidents” et prend en paramètre un dossier. Nous avons initialisé une liste “noms_presidents”, puis nous parcourons chaque discours dans le dossier “spechees”. Si le type du fichier se termine par “.txt”, alors nous utilisons les “split” pour délimiter la partie du titre du fichier qui nous intéresse. Le [1] sert à prendre la partie après le caractère indiqué (ici, “_”) et le [0] sert à prendre la partie avant le caractère indiqué (ici, le “.”). Enfin, nous ajoutons ce que nous venons de délimiter à la liste “noms_presidents” et nous renvoyons la liste. 


# 1.2 - Associer à chaque président un prénom
Pour la deuxième fonction, nous associons à chaque président un prénom. La fonction s’appelle “attribution_prenom” et prend en paramètre une liste. Pour cela nous initialisons un dictionnaire, qui à chaque clé (nom) va associer une valeur (prénom) en parcourant chaque nom dans la liste. Ensuite, nous utilisons des “if” et “elif” pour l’attribution des prénoms en fonction des noms. Enfin, nous renvoyons le dictionnaire.

Pour la troisième fonction, nous devons afficher la liste des noms des présidents (sans doublons). La fonction s’appelle “liste_sans_doublons” et prend en paramètre une liste. Pour cela nous initialisons une liste “L”. Ensuite nous parcourons dans la liste en paramètre chaque élément. Avec des “slices”, nous cherchons à savoir s’il existe plusieurs discours (éléments se terminant par un chiffre). Si c’est le cas, on enlève le dernier caractère de cet élément avec [:-1] et si cet élément n’est pas dans la liste “L” et que son dernier caractère est un chiffre, on l’ajoute. Sinon, si l’élément n’est pas dans la nouvelle liste et que son dernier caractère n’est pas un chiffre (cas ou il n’y a pas de doublons), on l’ajoute à la liste “L”. Enfin nous renvoyons la liste “L”.


# 1.3 - Afficher la liste des noms des présidents (sans doublons)
On affiche la liste des présidents sans les doublons grâce à l'appel des fonctions précédentes


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


# III - Fonctionnalités à développer
# 3.1 - Afficher la liste des mots les moins importants dans le corpus de documents (TD-IDF = 0 dans tous les fichiers)
La fonction "mots_non_importants" a pour objectif d'afficher la liste des mots les moins importants dans le corpus de documents, c'est-à-dire ceux ayant un score TF-IDF égal à 0 dans tous les fichiers. POur le faire la fonction prend en paramètre la matrice TF-IDF (matrice) générée précédemment. Elle répète sur chaque ligne de la matrice, représentant un mot. Pour chaque mot, elle calcule la somme de ses scores TF-IDF dans tous les fichiers. Et si la somme est égale à 0, cela signifie que le mot a un score TF-IDF nul dans tous les fichiers, et il est ajouté à la liste des mots non importants.


# 3.2 - Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé
La fonction "mots_importants" a pour objectif d'afficher les mots ayant le score TF-IDF le plus élevé parmi tous les fichiers. La fonction prend en paramètre la matrice TF-IDF (matrice) générée précédemment. Elle répète sur chaque ligne de la matrice, représentant un mot. Elle recherche le score TF-IDF le plus élevé parmi tous les fichiers. Et pour finir, elle identifie les mots ayant ce score et les ajoute à la liste des mots importants.


# 3.3 - Indiquer le(s) mot(s) le(s) plus répété(s) par un président (dans le test, Chirac)
La fonction "mots_repetes" a pour objectif d'indiquer les mots les plus répétés par un président donné. La fonction prend en paramètre le nom du fichier (fichier) correspondant au discours d'un président. Elle utilise la fonction TF pour obtenir le nombre d'occurrences de chaque mot dans le fichier. Elle identifie le score le plus élevé parmi les occurrences de chaque mot. Et ensuite, elle ajoute à la liste tous les mots ayant ce score.


# 3.4 - Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
La fonction "apparition_mot" a pour objectif d'indiquer les noms des présidents qui a ontt parlé de la "Nation" et celui qui l’a répété le plus de fois. Ainsi la fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche sera effectuée et le mot à rechercher (mot_recherche). Elle utilise la fonction "list_of_files" pour obtenir la liste des fichiers du dossier. Elle utilise la fonction "extraire_noms_presidents" pour obtenir la liste des noms des présidents à partir des noms de fichiers. Elle initialise un dictionnaire vide (dictionnaire) qui stockera le nombre d'occurrences du mot recherché par président. Elle parcourt chaque fichier du dossier et et ensuite utilise la fonction TF pour obtenir le nombre d'occurrences du mot recherché, et stocke ces informations dans le dictionnaire pour enfin identifié la liste des présidents qui ont parlé du mot. Elle détermine le président qui a répeté le mot le plus de fois en comparant les occurrences dans le dictionnaire.


# 3.5 - Indiquer le premier président à parler du climat et/ou de l’écologie
La fonction premier_a_parler a pour objectif d'indiquer le premier président à parler du climat ou de de l’écologie. La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche sera effectuée et le mot à rechercher (mot_recherche). Elle utilise la fonction "list_of_files" pour obtenir la liste des fichiers du dossier. Elle initialise un dictionnaire vide (dictionnaire) qui stockera l'indice de la première occurrence du mot recherché par président. Elle parcourt chaque fichier du dossier, utilise la fonction TF pour obtenir le nombre d'occurrences du mot recherché, et stocke l'indice de la première occurrence dans le dictionnaire.  Et enfin ellle identifie le président qui a mentionné le mot en premier en comparant les indices dans le dictionnaire.


# 3.6 - Hormis les mots dits « non importants », liste de(s) mot(s) que tous les présidents ont évoqués
L'objectif de la fonction "mots_evoques" est de lister les mots que tous les présidents ont évoqués, sauf les mots "non importants" (ceux avec un score TF-IDF de 0 dans tous les fichiers). La fonction prend en paramètre le nom du dossier (dossier) contenant les fichiers sur lesquels la recherche se base. Elle utilise la fonction  "list_of_files" pour obtenir la liste des fichiers du dossier. Elle utilise la fonction TF pour obtenir la fréquence d'apparition de chaque mot dans le premier fichier de la liste (file_list[0]), qui sert de référence. Elle initialise une liste vide (liste) qui stockera les mots évoqués par par tous les présidents. Elle parcourt chaque mot dans le dictionnaire de fréquence de référence. Pour chaque mot, elle vérifie s'il est présent dans la fréquence d'apparition de chaque président (dans chaque fichier du dossier). Si le mot est présent dans tous les fichiers, elle l'ajoute à la liste des mots évoqués par tous les présidents et retourne la liste.


# Partie II
# 1 - Tokenisation de la question
La fonction "transformer_en_liste_de_mots_une_chaine" a pour objectif principal de prendre une chaîine de caractères en entrée et de renvoyer une liste contenant tous les mots présents dasns cette cahîne.

Dans cette fonction, on initialise d'abord une liste vide "liste = []".
Cette liste va contenir les mots extraits de la chaîne, et une chaîne de caractères vide (mot) qui servira à construire les mots au fur et à mesure du parocurs de la chaîne;
La fonction parcourt chaque caractère de la chaîne d'entrée à l'aide de la boucle 'for'.

On vérifie ensuite si le caractère est alphabétique (s'il se situe entre 'a' et 'z' ou 'A' et 'Z') à l'aide de 'isalpha'. Si le caractère est alphabétique, il est ajouté à la fin du mot en cours de contsruction (mot) et tous les caractères alphabétiques sont convertis en minuscule avec 'lower'. Puis on retounrne la liste à la fin.


# 2 - Recherche de mots de la question dans le Corpus
La fonction "recherche_mots_corpus" commence par appeler de la fonction "transformer_en_liste_de_mots_une_chaine(question)", qui transforme la chaine de caractères de la question en une liste de mots.
Ensuite la fonction crée une maatrice TF IDF à partir du corpus en appelant la focntion TF_IDF(dossier).
La fonction parcourt chaque mot de la liste obtenue à partir de la question (liste) et parcourt ensuite chque ligne de la matrice TF-IDF. Si le mot est préent dans une ligne d ela matrice, il est ajouté à la liste liste_mots_du_corpus. La fonction retourne la liste liste_mots_du_corpus qui contient le smots de la question qui sont présent.

# 3 - Calcul de vecteur TF-IDF pour les termes de la question

La fonction TF_IDF a pour objectif de calculer la matrice TF-IDF pour chaque terme dans chaque document du corpus. 
La fonction "TF_IDF_2" commence par obtenir une liste de fichiers texte présents dans le dossier spéifié en appelant la fonction list_of_files(dossier, ".txt"). 
Ces fichiers représentent les documents du corpus. Ensuite, elle initialise une matrice vide qui sera remplie avec les valeurs TF-IDF. Chaque ligne de cette matrice représente un terme, et chaque colonne représente un document. Pour chaque terme dans le corpus, la fonction  utilise la fonction TF(fichier, dossier) pour calculer le nombre d'occurrences de ce terme dans chaque document. Elle utilise également la  fonction IDF(dossier) pour calculer le score IDF du terme dans l'ensemble du corpus. La fonction remplit remplit la matrice avec les valeurs TF-IDF calculées pour chaque terme dans chaque document. Chaque élément de la matrice représente le score TF-IDF d'un terme dans un document spécifique. Enfin, la  fonction renvoie la matrice complète, où chaque ligne correspond à un terme et chaque colonne correspond à un document, avec les valeurs TF-IDF calculées.

La fonction vecteur_TF_IDF vise à calculer le vecteur TF-IDF pour les termes présents dans une question spécifiée. Ce vecteur représente l'importance relative de chaque terme dans la question par  rapport à l'ensemble du corpus. La fonction utilise la fonctionn transformer_en_liste_de_mots_une_chaine  pour obtenir une liste de mots à partir de la question. Cette liste contient tous les termes de la question, sans doublons.

Pour chaque terme dans la liste obtenue, la fonction calcule le score TF en comptant combien de fois ce terme apparaît dans la question. Le score tf, représente la fréquence d'un terme dans une question, ce qui équivaut à diviser le nombre d'occurrences du terme par la longueurr totale de la liste de mots de la question.

En utilisant la fonction IDF(dossier), la fonction calcule le score IDF pour chaque terme présent dans la liste de mots. Le score TF-IDF est obtenu en multipliant le score TF par le score IDF correspondant à chaque  terme. La fonction assemble les scores TF-IDF calculés pour chaque terme dans la liste de mots, et produit un vecteur TF-IDF. La fonction renvoie le vecteur TF-IDF résultant, où chaque élément du vecteur correspond à l'importance d'un terme dans la question.


# 4- Calcul de la Similarité
La fonction produit_scalaire(vecteur1, vecteur2) calcule le produit scalaire entre deux vecteurs. Tout d'abord, c'est quoi un produit scalaire: le produit scalaire entre deux vecteurs est défini comme la somme des produits de leurs composantes correspondantes. La fonction commence par vérifier si les deux vecteurs ont la même dimension. Si ce n'est pas le cas, la fonction renvoie un message indiquant que les vecteurs ne peuvent pas être comparés. Si les vecteurs ont la même dimension, la fonction calcule le produit scalaire en itérant sur chaque composante des vecteurs et en accumulant la somme des produits.
La fonction renvoie le résultat du produit scalaire .

La fonction norme_vecteur(vecteur) a pour objectif de calculer la norme d'un vecteur. La norme d'un vecteur est la racine carrée de la somme des carrés de ses composantes.
La fonction commence par initialiser une variable, somme, à zéro. Cette variable va stocker la sommme des carrés des composantes du vecteur.
La fonction itère sur chaque composante du vecteur, élève chaque composante au carré, et ajoute le résultat à la somme. Une fois que la somme des  carrés est obtenue, la fonction calcule la racine carrée de cette somme. Cela donne la norme du vecteur. La fonction renvoie la valeur calculée, qui représente la norme du vecteur.

La fonction calcul_similarite a pour objectif de mesurer la similarité cosinus entre deux vecteurs. Elle évalue dans quelle mesure ces vecteurs pointent dans la même direction dans l'espace vectoriel. La fonction commence par calculer le produit scalaire entre les deux vecteurs V1 et V2 à l'aaide la fonction produit_scalaire. Ensuite, la fonction calcule les normes des deux vecteurs à l'aide de la focntion norme_vecteur.  En utilisant le produit scalaire et les normes des vecteurs, la fonction  calcule la similarité cosinus à l'aide de la formule : 
Produit Scalaire/Norme(V1).Norme(V2) La fonction renvoie la similarité cosinus


# 5- Calcul du document le plus pertinent
La fonction vise à déterminer quel document dans la matrice (représentant les documents originaux) est  leplus similaire à la question posée, en utilisant le calcul du produit scalaire entre les vecteurs TF-IDF. 
La fonction commence par initialiser un dictionnaire vides (dictionnaire) qui sera utilisé pour stocker les mesures de similarité entre le vecteur de la question et les vecteurs de chaque document.
La fonction itère sur chaque ligne de la matrice  (représentant les vecteurs TF-IDF des documents) et calcule le produit scalaire entre le vecteur de la question et chaque vecteur de document.
Les mesures de similarité sont stockées dans le dictionnnaire, qui  associe chaque document à sa mesure de similarité.
La fonction utilise la fonction cle_associee_a_val_max_dictionnaire (qui retourne la clé associée à la plus grande valeur dans le dictionnaire) pour déterminer quel document a la mesure  de similarité la plus élevée.
La fonction renvoie le document le plus simimlaire à la question, basé sur le produit scalaire des vecteurs.


# 6 - Génération d'une réponse
La fonction generation_reponse(question, dossier, dossier_origine) a pour objectif de générer une réponse à une question en utilisant la similarité entre le vecteur de la question et les vecteurs des documents dans la matrice TF-IDF. La réponse est générée en identifiant le document le plus similaire à la question et en extrayant une phrase pertinente de ce document.

La fonction utilise la fonction vecteur_TF_IDF pour calculer le vecteur TF-IDF de  la  question, représentant la question dans l'espace des termes du corpus.
La fonction utilise la fonction TF_IDF pour calculer la matrice TF-IDF des documents dans le dossier spécifié.
La fonction utilise la fonction similarite_documents_et_vecteurs pour identifier le document le plus similaire à la question, basé sur la similarité entre les vecteurs.
La fonction utilise la fonction vecteur_TF_IDF pour identifier le mot ayant le score TF-IDF le plus élevé dans la question. Ce mot est utilisé pour extraire une phrase pertinente du document le plus similaire.
La fonction lit le contenu du document le plus similaires (dans le dossier d'origine) et identifie la première phrase contenant le mot important.

La question est d'abord transformée en une liste de mots à l'aide de la fonction transformer_en_liste_de_mots_une_chaine(question). Chaque mot est extrait de la question et ajouté à la liste.
La fonction IDF(dossier) est utilisée pour calculer l'IDF  de chaque mot dans le corpus de documents spécifié par le dossier.
Un dictionnaire tf_question est créé pour stocke r le score TF-IDF de chaque mot de la question. Le score TF-IDF est calculé en comptant le nombre d'occurrences de chaque mot dans la quesstion  et en normalisant par la longueur de la question.
Création d'un dictionnaire des sscores TF-IDF pour chaque mot du corpus :
Un dictionnaire "dictionnaire" est créé pour associer chaque mot du corpus (calculé à partir de l'IDF) à son score TF-IDF dans la question. Si un mot n'est pas présent dans la question, son score est mis à zéro.

La fonction cle_associee_a_val_max_dictionnaire(dictionnaire) est utilisée pour identifier le mot ayant le score TF-IDF le plus élevé dans la question. Ce mot est considéré comme le mot le plus important dans le contexte de la question.
Le mot important est recherchéé dans le contenu de ce document.
Le contenu du   document est lu, et les phrases  sont extraites en utilisant des séparateurs tels que '.', '!', '?'.
La première phrase contenant le mot important est identifiée, et cette phrase est renvoyée comme résultat.
On veut à identifier le mot le plus important dans la question, puis à rechercher ce mot dans le document le plus similaire pour extraire une phrase associée à ce mot. 


# 7 - Affiner une réponse
La fonction affinage_reponse(question, dossier, dossier_origine) a pour objectif d'affiner la réponse générée en ajoutant une formulation initiale basée sur le type de question posée.
Une liste appelée question_starters est définie, et associe des formulations à différents types de questions (par exemple, "Comment", "Pourquoi", "Peux-tu").
La fonction generation_reponse est appelee avec la question, le dossier contenant les documents, et le dossier d'origine pour générer une réponse de base.
La fonction itère sur les formulations initiales dans la liste question_starters pour vérifier si la question commence par l'une de ces formulations.
Si une correspondance est trouvée, la réponse de base est précédée par la formulation initiale correspondante.
La réponse est renvoyée comme résultat final.
En résumé, la fonction affinage_reponse apporte une formulation initiale à la réponse générée en fonction du type de question posée.


# Fichier menu.py
On demande à l'utilisateur de choisir entre les fonctionnalités de la Partie 1 ou le ChatBot. Pour cela, on lui demande de saisir un chiffre, 1 pour les fonctionnalités de la Partie 1 ou 2 pour le chatBot, et cette valeur va etre stockée dans "choix". Maintenant, trois posibiltés s'offre à l'utilisateur:
# Première Possibilité:
La première possibilité est que l'utilisateur ait entré 1. Alors, on va maintenant lui demander le numéro de la question qu'il souhaite. Là encore, plusieurs choix sont possibles. Les choix peuvent aller du chiffre 1 à 6 et aussi la possibilité que l'utilisateur saisisse un numéro ou un caractère autre que les chiffres entre 1 et 6, et dans ce cas, il va s'afficher "Le numéro de l'exercice ne correspond pas.". Maintenant, on s'intéresse aux questions allant de 1 à 6, mais avant cela, on initialise "matrice_test" au "TF_IDF_Test".

-La première question cherche à renvoyer tous les mots dits "non importants", c'est-à-dire, un mot où son TF-IDF = 0 dans tous les fichiers. Pour cela, on se sert de la fonction "mots_non_importants" avec comme paramètre "matrice_test" (cette fonction est expliquée au 3.1 plus haut). On va ensuite afficher la liste que la fonction nous renvoie, c'est-à-dire les mots non importants.

-Pour la deuxième question, on cherche à afficher les mots ayant le score TF-IDF le plus élevé. Cette fois-ci, on va utiliser la fonction "mots_importants" (expliquée plus haut, 3.2) avec comme paramètre "matrice_test" également. Cette fonction va ensuite nous renvoyer une liste que l'on va afficher, et nous aurons les mots les plus importants.

-Pour la troisième question, le but est d'afficher les mots les plus répétés par le président Chirac, hormis les mots dits "non importants". Pour cela, on va utiliser la fonction "mots_repetes" (expliquée plus haut, 3.3). On va affecter à une première liste (liste 1) les mots les plus répétés de son premier discours. La deuxième liste (liste 2) utilise la même fonction mais avec son deuxième discours. Puis on va affecter une troisième liste (liste 3) qui est initialisée comme la première liste. On va ensuite vérifier à l'aide d'une boucle si les mots de la deuxième liste (liste 2) sont dans la troisième liste (liste 3). Si ce mot n'est pas dans la troisième liste, alors on l'ajoute à la troisième liste. On va ensuite afficher cette dernière et il s'affichera tous les mots les plus répétés, hormis les mots les moins importants, par le président Chirac.

-Pour la quatrième question, on cherche à savoir qui a parlé de la "Nation" et qui l'a répété le plus de fois. Pour cela, nous allons appeler la fonction "apparition_mot" (expliquée plus haut, 3.4) avec comme paramètres le fichier avec tous les discours et le mot à chercher, ici, "Nation". Une fois la fonction appelée, elle va nous renvoyer les présidents qui ont parlé de la Nation et celui qui en a le plus parlé.

-Pour la cinquième question (première partie du projet, avant modification de la question), on cherche à savoir qui a parlé du climat en premier. Pour cela, on utilise la fonction "premier_a_parler" (expliquée plus haut, 3.5) avec comme paramètres le fichier avec tous les discours et le mot recherché : climat. Il va ensuite s'afficher le nom du premier président ayant parlé du climat, ainsi que l'indice où il en parle en premier.
  
-Pour la dernière question, on cherche les mots les plus évoqués par les présidents. On utilise la fonction "mots_evoques" (expliquée plus haut, 3.6) avec comme paramètre le fichier avec tous les discours. On va ensuite afficher cette liste. La fonction renvoie le même résultat que la première fonction 'mots_non_importants' car ce sont des mots qui sont utilisés dans les discours de chacun.

# Deuxième Possibilité 
La deuxième possibilité est que l'utilisateur ait entré 2, alors on va lui demander de saisir sa propre question. On va ensuite utiliser la fonction "affinage_reponse" (expliquée plus haut, Partie II) avec comme paramètres la question choisie par l'utilisateur et les fichiers contenant les discours des présidents. On va ensuite afficher la réponse donnée.


# Dernière Possibilité 
La dernière possibilité est que l'utilisateur ait entré une valeur autre que 1 ou 2, et il va alors s'afficher "Le numéro sélectionné n'existe pas."

# FIN 







