# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:39:41 2020

@author: derbaghc
"""

import numpy as np
from random import *


def average_above_zero(table: list):
    """
    Fonction qui calcule la moyenne des valeurs d'un tableau donné, en 
    sélectionnant seulement les valeurs positives
    param:
        tab : tableau donné par l'utilisateur
    returns:
        average : moyenne avec les valeurs positives de tab
    """
    sum = 0
    n = 0
    tab_size = len(table)
    for x in range(0, tab_size):
        """Check if our value is positive"""
        if table[x] > 0:
            sum += table[x]
            n += 1
        else:
            raise Exception("Can't be below 0. The value of x was: {}".format(x))
    average = sum / n
    return average


# print(average_above_zero([1, -2, 3]))


"""
Q1 / Si on oublie l'initialisation de la variable on ne pourra pas l'utiliser 
dans le for ensuite.
"""

"""
Q2 / Si toutes les variables sont en dessous de 0, on ne passe pas dans le if, 
et donc on essaye de faire une division par 0 ce qui renvoie une erreur.
"""


def max_value(tab: list):
    """
    Fonction qui renvoie la valeur max d'un tableau ainsi que son index
    param:
        tab : tableau donné par l'utilisateur
    returns:
        max_var : valeur max du tableau
        max_var_index : index de la valeur max du tableau
    """
    """
    version courte :
    max_var = max(tab)
    max_var_index = tab.index(max_var)
    return max_var, max_var_index
    """
    size = len(tab)
    max_var = tab[0]
    max_var_index = 0
    for i in range(size):
        if(tab[i] > max_var):
            max_var = tab[i]
            max_var_index = i
    return max_var, max_var_index

#print(max_value([1, 7, 3]))


def reverse_table(tab: list):
    """
    Fonction qui inverse le tableau
    param:
        tab : tableau donné par l'utilisateur
    returns:
        tab : tableau inversé

    """
    """
    méthode courte: 
    tab = tab[::-1]
    return tab;
    """
    size = len(tab)
    for i in range(size//2):
        tmp = tab[i]
        last = (size-1) - i
        tab[i] = tab[last]
        tab[last] = tmp
    return tab

#print(reverse_table([1, 2, 3]))


def roi_bbox(input_image):
    """
    Fonction qui encadre une zone définie de 1
    param:
        input_image : matrice donnée de 0 avec une zone de 1
    returns:
        z : coordonées de la forme encadrant les 1
    """

    # Tableaux
    rows = np.where(input_image == 1)[0]  # renvoie les coordonnées x des 1
    cols = np.where(input_image == 1)[1]  # renvoie les coordonnées y des 1

    # Each coordinates
    left_up = [rows[0], cols[0]]
    left_down = [rows[-1], cols[0]]
    right_up = [rows[0], cols[-1]]
    # -1 récupère la dernière valeur du tableau
    right_down = [rows[-1], cols[-1]]

    # Return
    z = ([left_up, right_up], [right_down, left_down])
    return z


rows = 5
cols = 5
input_image = np.zeros((rows, cols))
input_image[1:3, 2:5] = np.ones((2, 3))
# print(input_image)
#print(roi_bbox(input_image))


def alea(n):
    """
    Fonction qui tire aléatoirement un chiffre en 0 et n
    param:
        n : nombre max. On choisira aléatoirement un chiffre entre 0 et n
    returns:
        nb : nombre aléatoire
    """
    """
    version courte :
    """
    return randint(0, n)


def random_fill_sparse(tab, k: int):
    """
    Fonction qui remplit un table de N*N avec des 'X' à des positions 
    aléatoires
    param:
        tab : tableau donné
        k : nombre de cellules à remplir de valeurs aléatoires
    returns:
        z : coordonées de la forme encadrant les 1
    """
    nbX = 0
    while nbX < k:
        row = tab[alea(len(tab) - 1)]
        random = alea(len(row) - 1)
        if row[random] == "X":
            pass
        else:
            row[random] = "X"
            nbX += 1
    return tab


tab = np.empty((5, 5), dtype=str)


# print(tab)
# print(random_fill_sparse(tab, 4))


def remove_whitespace(string: str):
    """
    Fonction qui supprime les espaces dans une string
    param:
        string : chaine de caractères
    returns:
        string.replace : renvoie la phrase sans les espaces
    """
    """
    version courte :
    return string.replace(' ', '')
    """
    res = ""
    for spaces in string:
        #si le caractère est différent d'un espace, on l'ajoute à notre réponse
        if(spaces != " "):
            res += spaces
    return res

string = "Coucou tout le monde"

#print(remove_whitespace(string))


def shuffle(list_in):
    """
    Fonction qui mélange les éléments d'une liste
    param:
        list_in : liste d'éléments
    returns:
        random.shuffle(list_in) : renvoie la liste mélangée aléatoirement
        version longue : list_in -> renvoie la liste mélangée
    """
    """
    version courte :
    return random.shuffle(list_in)
    """
    size = len(list_in)
    for i in range(size):
        nb = alea(size-1)
        tmp = list_in[nb]
        list_in[nb] = list_in[i]
        list_in[i] = tmp
    return list_in

#print(shuffle([1, 2, 3, 4, 5, 6]))

'''     
for a in range(2,5):
    for b in range(1, 3):
        input_image[b, a] = 1
print(input_image)
'''

'''
input_image[1:3,2:4] = np.ones((2, 3))
'''

"""
SORTING
"""

"""
Selective sort
"""
"""
a) Illustration du tri par sélection sur 10, 15, 7, 1, 3, 3, 9
    1. On recherche sur 0 - 6 le minimum : c'est 1
    On a 1, 15, 7, 10, 3, 3, 9
    
    2. Sur 1 - 6 le minimum : 3
    On a 1, 3, 7, 10, 15, 3, 9
    
    3. Sur 2 - 6 le minimum : 3
    On a 1, 3, 3, 10, 15, 7, 9
    
    4. Sur 3 - 6 le minimum : 7
    On a 1, 3, 3, 7, 15, 10, 9
    
    5. Sur 4 - 6 le minimum : 9
    On a 1, 3, 3, 7, 9, 10, 15
    
    6. Sur 5 - 6 le minimum : 10 
    Le tableau était déjà trié. Fin. 
"""

"""
Fonction qui trie une liste avec la méthode du tri par sélection.
param : list_in de type list
return : list_in
"""
def selection_sort(list_in:list):
    size = len(list_in)
    permutations = 0
    comparisons = 0
    for i in range(size-1):
        index_min = i
        tmp = list_in[i]
        for j in range(i+1, size):
            if(list_in[index_min] > list_in[j]):
                index_min = j
                comparisons += 1
        # permet d'intervertir deux valeurs
        list_in[i], list_in[index_min] = list_in[index_min], list_in[i]
        permutations += 1
    print("permutations : " +str(permutations))
    print("comparisons : " + str(comparisons))
    return list_in

#list = [10, 15, 7, 1, 3, 3, 9]
#list=[alea(100) for i in range(100)]
#print(selection_sort(list))

"""
b) Oui, le nb d'itérations dépend du contenu. 
c) Dans ce cas là, 6, donc j'en déduis qu'il en faut le nombre de la taille. 
d) Ici on a fait 5 permutations. 
e) On a fait 8 comparisons.
f) Il a une complexité O(n2).
g) Le nombre de permutations est toujours égal à size-1 mais le nombre de comparaison dépend à mon avis
   des valeurs du tableau.
"""

"""
Bubble sort 
"""
"""
a) Illustration du tri par bulles sur 10, 15, 7, 1, 3, 3, 9
    Premier passage pour mettre le maximum à la fin. 
        1. On compare sur 0 - 1 le minimum : c'est 10
        On a 10, 15, 7, 1, 3, 3, 9
    
        2. Sur 1 - 2 le minimum : 7
        On a 10, 7, 15, 1, 3, 3, 9
    
        3. Sur 2 - 3 le minimum : 1
        On a 10, 7, 1, 15, 3, 3, 9
    
        4. Sur 3 - 4 le minimum : 3
        On a 10, 7, 1, 3, 15, 3, 9
    
        5. Sur 4 - 5 le minimum : 3
        On a 10, 7, 1, 3, 3, 15, 9
    
        6. Sur 5 - 6 le minimum : 9 
        On a 10, 7, 1, 3, 3, 9, 15. Le maximum est remonté.  
    Deuxième passage :
        1. On compare sur 0 - 1 le minimum : 7
        On a 7, 10, 1, 3, 3, 9, 15
    
        2. Sur 1 - 2 le minimum : 1
        On a 7, 1, 10, 3, 3, 9, 15
    
        3. Sur 2 - 3 le minimum : 3
        On a 7, 1, 3, 10, 3, 9, 15
    
        4. Sur 3 - 4 le minimum : 3
        On a 7, 1, 3, 3, 10, 9, 15
    
        5. Sur 4 - 5 le minimum : 9
        On a 7, 1, 3, 3, 9, 10, 15. 
    Troisième passage :
        1. On compare sur 0 - 1 le minimum : 1
        On a 1, 7, 3, 3, 9, 10, 15.
    
        2. Sur 1 - 2 le minimum : 3
        On a 1, 3, 7, 3, 9, 10, 15
    
        3. Sur 2 - 3 le minimum : 3
        On a 1, 3, 3, 7, 9, 10, 15
    
        4. Sur 3 - 4 le minimum : 7
        On a 1, 3, 3, 7, 9, 10, 15 
    Quatrième passage :
        Le tri passe et voit que la liste est bien triée, il s'arrête.         
"""

"""
Fonction qui trie une liste avec la méthode du tri à bulles.
param : list_in de type list
return : list_in
"""
def bubble_sort(list_in:list):
    size = len(list_in)
    iterations = 0
    permutations = 0
    comparisons = 0
    for i in range(size-1):
        #on met -i car le max est placé on a plus besoin d'y toucher
        iterations += 1
        for j in range(0, size-1-i):
            iterations += 1
            if(list_in[j] > list_in[j+1]):
                comparisons += 1
                #permet d'intervertir deux valeurs
                list_in[j], list_in[j+1] = list_in[j+1], list_in[j]
                permutations += 1
    print("iterations : " + str(iterations))
    print("comparisons : " + str(comparisons))
    print("permutations : " + str(permutations))
    return list_in

#list = [10, 15, 7, 1, 3, 3, 9]
#list=[alea(500) for i in range(500)]
#print(bubble_sort(list))

"""
b) Oui, plus il y aura de valeurs, et plus il y aura d'itérations pour mettre le max à la fin
c) Pour la liste de 6 valeurs, on a 27 itérations (6 pour la première boucle et 21 pour la deuxième).
Cela correspond aux passages de l'illustration ci-dessus
d) Il y a eu 13 permutations, 2 fois la longueur du tableau moins 1 car on ne permute pas la dernière case, 
le maximum remonte de lui-même lors du premier passage.
e) Il y a eu 13 comparisons, pour la même raison que les permutations. 
f) Je dirais que la complexité de cet algorithme est de 0(n2) 
g) Le nombre d'itérations correspond à peu près au double de permutations et de comparaisons. 
Les permutations et les comparaisons sont toujours égales, mais beaucoup plus importantes que le tri par sélection.
"""

