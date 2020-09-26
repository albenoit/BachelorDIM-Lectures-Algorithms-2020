# Average
def average(tab):
    """
    Calculate the average of a list
    Parameters
        tab
    Returns the average of the list
    """
    som = 0
    n = 0
    for i in range(len(tab)):
        if tab[i] > 0:
            som = som + tab[i]
            n = n + 1
    moy = som / n
    print(moy)


average([100, 20, 30])


# Maximum value
def max_value_in_tab(tab):
    """
    Get the maximum value of a tab
    Parameters
        tab
    Returns the maximum value of a tab
    """
    max = tab[0]
    for a in tab:
        if a > max:
            max = a
    return max


print(max_value_in_tab([1, 12, -8, 300]))


# Reverse a table
tab = [100, 'abc', 437, 'def', 123]
tab.reverse()
print(tab)

# Reverse a table V2
def reverse_table(tab):
    """
        Reverse a table
        Parameters
            table of numbers
        Returns reversed table
    """
    for i in range(len(tab)//2):
        list_len = len(tab)
        tmp = tab[i]
        endid = list_len - i - 1
        tab[i] = tab[list_len - 1]
        tab[i] = tab[endid]
        tab[endid] = tmp
    return tab


print(reverse_table([100, 200, 300, 400]))


# Bounding box

import numpy as np

def bounding_box(matrix):
    """
    Compute the bounding box coordinates of an object
    Parameters
        matrix
    Returns numpy array of shape 4x2 filled with the four 2d coordinates
    """
    w = matrix.shape[1]
    h = matrix.shape[0]
    x1 = w
    y1 = h
    x2 = 0
    y2 = 0
    for x in range(w):
        for y in range(h):
            if matrix[y, x]:
                if x < x1:
                    x1 = x
                    print("bound entry x1: ", x1)
                if y < y1:
                    y1 = y
                    print("bound entry y1: ", y1)
                if x2 < x:
                    x2 = x
                    print("bound entry x2: ", x2)
                if y2 < y:
                    y2 = y
                    print("bound entry y2: ", y2)

    return (x1, y1, x2, y2)

# Random array filling

#Remove whitespace characters in a string:
def remove_whitespace(string):
    """
        Parse a string and remove all its whitespace
        Parameters
            string
        Returns string without whitespaces
    """
    return string.replace(" ", "")


string = ' l p d i m '
print(remove_whitespace(string))

# Random item selection
import random

def random_item(list:any):

    """
         Randomly select item of a list
         Parameters
             list
         Returns one item of the list
    """
    return random.choice(list)


list = 1, 6, "b", 12, "k", 8, "LP DIM", 2020, "Overkiz", "Hr Team"
print(random_item(list))

# Personal test for testing numpy with Pycharm
a = np.array([1, 2, 4])
print(a)

# My Addition function
def my_addition(a, b):
    return a+b

print('10+2=12 ?',my_addition(10,2))
