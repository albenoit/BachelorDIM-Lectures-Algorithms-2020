"""
Created by Yoan ROULEAU
@author: myself
"""
import numpy as np

def average_above_zero(array):
    '''
    Receives an array as a parameter and calculates its average.

    :arg
        array: an array
    :returns
        moy: Its average
    '''
    som = 0
    positive_element_count=0
    for i in array:
        if i > 0:
            som += i
            positive_element_count+=1

    if positive_element_count > 0:
        average = som/positive_element_count
    else:
        raise ValueError('No positive values found in the array.')
    return average


def max_value(array):
    '''
        Receives an array as a parameter and returns is biggest value

        :arg
            array: an array
        :returns
            max: the biggest value of the array
    '''
    max = 0
    for value in array:
        if value > max:
            max = value

    return max


def reverse_table(array):
    '''
        Gets an array and reverses its values.

        :param
            array: An array
        :return:
            Reversed array
    '''
    arrlength = len(array)
    for i in range(arrlength//2):
        tmp = array[i]
        endValueIndex = arrlength - i - 1
        array[i] = array[endValueIndex]
        array[endValueIndex] = tmp
    return array

def roi_bbox(matrix):
    '''


    :param
        matrix: A matrix
        w: matrix's width
        h: matrix's height
        x1: right bound x coord
        y1: right bound y coord
        x2: left bound x coord
        y2: left bound y coord
    :return:
        x1, y1, x2, y2
    '''
    w = matrix.shape[1]
    h = matrix.shape[0]
    x1 = w
    y1 = h
    x2 = 0
    y2 = 0
    x = 0
    y = 0
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
    return(x1, y1, x2, y2)


#def random_fill_parse():


H = 12
W = 10
matrix = np.zeros((H,W), dtype=bool)
for c in range(7, 10):
    for l in range(6, 9):
        matrix[l, c] = 1
matrix[2:4, 2:5] = np.ones((2, 3), dtype=bool)

Tab = [50, 1, 2, 85]
average = average_above_zero(Tab)
print('Average: ', average)
print('Max: ' + str(max_value(Tab)))
print('Reverse: ' + str(reverse_table(Tab)))

bbox = roi_bbox(matrix)
print(bbox)





"""
WHAT HAPPENS IF "SOM" INITIALIZATION IS FORGOTTEN ?
-> You get an error saying that Som isn't defined.

WHAT CAN YOU EXPECT IF ALL THE VALUES ARE BELLOW ZERO ?
-> If your values are bellow zero, you wont be able to access the average calculation since you're testing each 
values in the array are bellow zero. In the end, the function will attempt to divide 0 by 0 (default values), and throw
and error back.
"""

