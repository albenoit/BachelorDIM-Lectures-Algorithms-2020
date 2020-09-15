# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""



#Q1 : Si 'som' n'est pas initialisé, le code va planter lorsqy'on fait
#som = som + p_list[i] car lors de la première addition, som n'aura pas de valeur.

#Q2: Si la liste ne contient que des 0, alors le code va planter car n vaudra 0
#or on ne peut pas faire de division par 0.

#Fonction permettant de calculer la moyenne d'une liste dont la valeur est
#supérieur à 0

# @brief : permet de faire la moyenne d'une liste dont les valeurs supérieur à 0
# @param list contient une liste de nombre (float)
# @result affiche la moyenne (float)
def average_below_zero(p_list):
    som = 0
    n = 0
    for i in range(len(p_list)):
        if(p_list[i] > 0):
            n = n +1
            som = som + p_list[i]
    moy = som / n
    print(moy)