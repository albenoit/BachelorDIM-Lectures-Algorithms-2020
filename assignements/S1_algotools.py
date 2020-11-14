# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:04 2020

@author: cuvellin
"""
import numpy as np
import random


def average_above_zero(list_of_numbers):
    """
    One will to compute the average of the positive elements of a table.

    Parameters:
        list_of_numbers
    Raise:
        Can call a raise ValueError if n == 0
    Returns:
        average of the positive elements of a table
    """
    n = 0
    som = 0
    sizeArray = len(list_of_numbers)
    for i in range(sizeArray):
        if list_of_numbers[i] > 0:
            som += list_of_numbers[i]
            n = n + 1
    if n != 0:
        moy = som / n
    else:
        raise ValueError('ZeroDivisionError')
    return float(moy)


def max_value(array):
    """
    get the max value in array put in params

    Parameters:
        array
    Returns:
        max value in array put in params
    """
    max = None
    for i in array:
        if max is None or i > max:
            max = i

    return max


def reverse_table(tab):
    """
    reverse a table without the use of any other table

    Parameters:
        tab
    Returns:
        reverse of tab put in params
    """
    listlen = len(tab)

    for i in range(len(tab) // 2):
        tmp = tab[i]
        endid = listlen - i - 1
        tab[i] = tab[listlen - 1]
        tab[i] = tab[endid]
        tab[endid] = tmp
    return tab


def roi_bbox(input_image):
    """
    algorithm able to compute the bounding box coordinates of the object

    Parameters:
        input_image as numpy tab
    Returns:
        a numpy array of shape 4x1 filled with the four 2D coordinates
    """
    matrix_found_bb = np.where(input_image != False)

    if len(matrix_found_bb[0]) == 0 or len(matrix_found_bb[1]) == 0:
        raise ValueError('No pixel found')

    x1 = matrix_found_bb[0][0]
    y1 = matrix_found_bb[1][0]
    x2 = matrix_found_bb[0][len(matrix_found_bb[0]) - 1]
    y2 = matrix_found_bb[1][len(matrix_found_bb[1]) - 1]

    return np.array([x1, y1, x2, y2])


def random_fill_sparse(numpy_array, k):
    """
    an algorithm able to fill a specified number of K cells
    with 0X0 values at random positions while the others cells should remain empty

    Parameters:
        numpy_array
        k : number
    Returns:
        numpy_array with 'X'
    """
    if not is_square(numpy_array):
        raise ValueError('Your matrix is not a square')

    blank = np.where(numpy_array == '')  # get all values empty in numpy_array

    if k > len(blank[0]):
        raise ValueError('Not enough entry empty')

    list_random = random.sample(range(0, len(blank[0])), k)  # between 0 and k

    for i in range(k):
        numpy_array[blank[0][list_random[i]], blank[1][list_random[i]]] = 'X'

    return numpy_array


def is_square(m): return all(len(row) == len(m) for row in m)


def remove_whitespace(text: str):
    """
     algorithm able to parse a string and remove all its whitespace

    Parameters:
        numpy_array
        text : string
    Returns:
        string without space
    """
    new_text = ''
    for c in text:
        if c != ' ':
            new_text += c

    return new_text


def shuffle(list_in: list):
    """
     shuffle a list

    Parameters:
        list_in
    Returns:
        shuffle list
    """
    random_list_number = random.sample(range(0, len(list_in)), len(list_in))

    new_list = []
    for i in random_list_number:
        new_list.append(list_in[i])

    return new_list


"""
Tab = [4, 2, 45, -4, 14, -95, -4, 2, 87, -56, 65, 1, 3]
print("Averaging above zero : ", average_above_zero(Tab))

print("Reverse a table : ", reverse_table([1, 2, 3, 4, 5]))

print("Table maximum value : ", max_value([8, 9, 7, -9]))

matrix_bounding_box = np.array([[False, False, True, True, False, False, False, False, False, False],
                                [False, False, True, True, False, False, False, False, False, False],
                                [False, False, False, False, False, True, True, False, False, False],
                                [False, False, False, False, False, True, True, False, False, False],
                                [False, False, False, False, False, False, False, False, False, False]])

print("Bounding box : ", roi_bbox(matrix_bounding_box))

test_array = np.empty([3, 3], dtype=str)
print("random_fill_sparse : ", random_fill_sparse(test_array, 4))

print(remove_whitespace("ceci est un test"))

print(shuffle(['test1', 'test2']))

"""
