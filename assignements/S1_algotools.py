# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


"""
Session 1 Averaging 
"""

"""
Questions
What happens if Som initialization is forgotten ?
    if Som never existed then it will make an eror 
    if Som already existed before this code, then Sum will already have a value
    
What can you expect if all the values are below zero ?
    N value will be 0 and because we divide a number with N there will be an error 

Translate this algorithm in the python3.x language within script of name:
"""
def average_above_zero(Tab):
    '''
    This function return th average of all he numbers above 0 in array
    Parameters:
        Tab: a table of numner 
    Returns: a reversed table 
    Raises: an error if there is no positive values in the list (Tab)
    '''
    Som = 0
    N = 0 
    for i in Tab :
        if i > 0 :
            Som = Som + i
            N = N + 1
        if N>0:
            Moy = Som/N
        else:
            raise ValueError('division par zero')
    return Moy

print(average_above_zero([-1,-2]))



"""
Session 1 Table maximum value
"""

"""
Propose changes on the previous algorithm to get the maximum value of
a table.
"""
def  max_value_without_index(Tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        Tab: a list of number 
    Returns: highest value 
    '''
    Max = 0 
    for i in Tab :
        if i > Max :
            Max = Max                       
    return Max

print(average_above_zero([1,2,3]))
"""
Improve the previous changes by capturing the index of the last maximum
value.
"""
def  max_value(Tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        Tab: a list of number 
    Returns: highest value and it's index (highestvalue,Index)
    '''
    Max = 0 
    N=0
    Index = 0
    for i in Tab :
        if i > Max :
            Max = i
            Index = N
        N+=1     
                              
    return (Max,Index)

print(max_value([4,2,3]))

"""
Session 1 Reverse a table 
"""
def reverse_table(Tab):
    '''
    This function reverse a table
    Parameters:
        Tab: a table of numner 
    Returns: a reversed table 
    '''
    return Tab[::-1]
 
        
print(reverse_table([1,2,3,4,5,6]))

