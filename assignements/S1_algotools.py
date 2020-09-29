import numpy as np
import random

tab = [1,9,3,4,5,6,7,8,2]
np_tab = np.zeros((200,200))
np_tab[70:90,45:55] = np.ones((20,10))

def average_above_zero(tab:int):
    """
    This function calculate the average of list tab

    Parameters :
        tab: the list
    Returns :
        return the average of list
    """
    som = 0
    n = 0

    for i in tab:
        if i > 0:
            som += i
            n += 1

    if n > 0:
        return som / n
    else:
        raise ValueError('All numbers are <= 0')

def max_value(tab):
    """
    This function determine the max value of list tab

    Parameters :
        tab: the list
    Returns :
        return the max value of list
    """
    max_val = 0

    for i in tab:
        if i > max_val:
            max_val = i

    return max_val

def get_index_max_value(tab):
    """This function determine the index of max value of list tab

    Parameters :
        tab: the list
    Returns :
        return the index of max value of list
    """
    max_val = 0
    n = 0
    index = 0

    for i in tab:
        n+=1
        if i > max_val:
            max_val = i
            index = n

    return index

def reverse_table(tab):
    """
    This function reverse the table

    Parameters :
        tab: the list
    Returns :
        return the reverse table
    """
    for i in range(len(tab)//2):
        tmp = tab[i]
        endVal = len(tab)-i-1
        tab[i] = tab[endVal]
        tab[endVal] = tmp

    return tab

def bounding_box(np_tab):
    """
    This function determine a bounding box of true values

    Parameters :
        np_tab: the numpy array
    Returns :
        return the bounding box of true values
    """
    lx, ly = np.where(np_tab != 0)
    if lx is None or ly is None:
        raise ValueError('X or Y is null')
    else:
        return np.array([
            [np.min(lx),np.min(ly)],
            [np.max(lx),np.max(ly)]
        ])                                                                     

def alea(x,min=None):
    """
    This function generate a random number

    Parameters :
        x: max number
    Returns :
        return random nuumber
    """
    if min != None:
        return random.randint(min, x)
    else:
        return random.randint(0, x)

def random_array_fill(array,k):
    """
    This function fill random cells with X

    Parameters :
        array: the empty array
        k: number of X
    Returns :
        return array with random cells
    """
    for i in range(k):
        array[alea(array.shape[0]-1),alea(array.shape[1]-1)] = 'X'

    return array

def remove_whitespace(string):
    """
    This function remove space

    Parameters :
        string: the string
    Returns :
        return string witout space
    """
    return string.replace(' ','')

def shuffle(tab):
    """
    This function remove space

    Parameters :
        string: the string
    Returns :
        return string without space
    """
    array = []
    for i in range(len(tab)):
        random = alea(len(tab)-1)
        array.append(tab[random])
        tab.pop(random)
    return array
    
print(average_above_zero(tab))

"""
print(max_value(tab))
print(get_index_max_value(tab))
print(reverse_table(tab))
print(bounding_box(np_tab))
print(random_array_fill(np.empty([alea(30,2),alea(30,2)], dtype=str),alea(50,1)))
print(remove_whitespace('Python c\'est trop cool !'))
print(shuffle(tab))

"""