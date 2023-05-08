7 / 2
3.5
#Pour réaliser une division entière, il faut utiliser // :

7 // 2
3
#L’opérateur %
#L’opérateur % (appelé opérateur modulo) fournit le reste de la division entière d’un nombre par un autre.

#Exemple

7 % 2
1
6 % 2
0
#Affectation
a = 2
a
2
b = a + 3
b
5
#La première ligne contient l’instruction a = 2. Pour comprendre cette instruction, il faut imaginer que les informations sont stockées dans des boîtes au sein de la mémoire de l’ordinateur. Pour manipuler les informations, on donne des noms à ces boîtes. Ici on crée une boîte appelée a et on lui affecte la valeur 2. Par la suite, on parlera de la variable a, puisque a peut contenir des valeurs variables. Autrement dit, l’instruction a = 2 est une instruction d”affection qui a pour effet de mettre la valeur 2 dans la variable a.

#Affichage - la fonction print()
#Pour afficher, on utilise la fonction print().

print("bonjour")
bonjour
a = 5
print(a)
  5
#Il est possible de réaliser plusieurs affichages à la suite. Pour cela, on sépare les éléments par des virgules.

a = 5
print("a vaut", a)
a vaut 5
#Avertissement

#Pour ne pas aller à la ligne et continuer sur la même ligne lors du prochain print, on ajoute le paramètre end=" " :

print("a vaut", a, end=" ")
La fonction range()
Si vous avez besoin de créer sur une suite d’entiers, vous pouvez utiliser la fonction range(). Elle génère une suite arithmétique.

range(10)
range(0, 10)
En Python 3, si on souhaite afficher les valeurs, il est nécessaire de convertir le résultat en liste grâce à la fonction list(). Par exemple :

list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Le nombre de fin qui lui est passé n’est jamais dans la liste générée. Par exemple, range(10) génère 10 valeurs, exactement les indices des éléments d’une séquence de longueur 10. Il est possible de faire commencer l’intervalle à un autre nombre, ou de spécifier un incrément différent (même négatif) :

list(range(5, 10))
[5, 6, 7, 8, 9]
list(range(0, 10, 3))
[0, 3, 6, 9]
list(range(-10, -100, -30))
[-10, -40, -70]
De manière générale, on a :

range(valeur_initiale, borne_de_fin, pas)

Le pas peut être positif ou négatif. La valeur de la borne de fin (maximale ou minimale) n’est jamais atteinte.

Exercice

Créer une liste contenant les entiers pairs allant de 10 à 20.

Accès aux éléments d’une liste
a = list(range(1,10,2))
a
  [1, 3, 5, 7, 9]
a[0]
  1
a[2]
  5
Pour accéder à un élément d’une liste, on indique entre crochets [] l’indice de l’élément.

Avertissement

En Python, l’indice du premier élément d’une liste est 0 (ceci est à distinguer d’autres langages).

La fonction len()
La fonction len() renvoie le nombre d’éléments. Par exemple :

a = list(range(7,10))
a
[7, 8, 9]
len(a)
3
Lecture d’informations au clavier - la fonction input()
x = int(input("Donnez un entier : "))
Par défaut, la fonction input() renvoie une chaîne de caractères. Il faut donc utiliser la fonction int() qui permet d’obtenir un entier.

Autre exemple de programme
n = 3
print("Je vais vous demander", n, "nombres")
for i in range(n):
    x = int(input("Donnez un nombre : "))
    if x > 0:
        print(x, "est positif")
    else:
        print(x, "est négatif ou nul")
print("Fin")

Pour faire une répétition : l’instruction for

for i in range(n):
    bloc d'instructions
Pour faire un test : l’instruction if

if x > 0:
    print(x, "est positif")
else:
    print(x, "est négatif ou nul")
#Les différentes sortes d’instruction

#les instructions simples

#les instructions composées comme if ou for

#les blocs d’instructions

Voir aussi

https://python.developpez.com/cours/apprendre-python3/?page=page_5#L5

Règles générales d’écriture
Les identificateurs
Un identificateur est une suite de caractères servant à désigner les différentes entitées manipulées par un programme : variables, fonctions, classes…

En Python, un identificateur est formé de lettres ou de chiffres. Il ne contient pas d’espace. Le premier caractère doit obligatoirement être une lettre. Il peut contenir le caractère « _ » (underscore, en français « souligné »). Il est sensible à la casse (distinction entre majuscule et minuscule).

Les mots-clés
Les mots réservés par le langage Python (if, for, etc.) ne peuvent pas être utilisés comme identificateurs.

Voir aussi

Les commentaires
Les commentaires usuels:

# Ceci est un commentaire
Les commentaires en fin de ligne:

a = 2 # Ceci est un commentaire