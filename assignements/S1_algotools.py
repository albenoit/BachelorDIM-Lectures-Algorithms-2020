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
    bottomX = matrix.shape[0]
    bottomY = matrix.shape[1]
    topX = 0
    topY = 0
    for line in matrix:
        for value in line:
            if value == 2:
                print('yes')
            else:
                topX+=1
    print(topX)


Tab = [50, 1, 2, 85]
matrix = np.zeros((15,10))
for c in range(7, 10):
    for l in range(6, 9):
        matrix[l, c] = 1
matrix[2:4, 2:5] = np.ones((2, 3))*2

average = average_above_zero(Tab)
print('Average: ', average)
print('Max: ' + str(max_value(Tab)))
print('Reverse: ' + str(reverse_table(Tab)))

bbox = roi_bbox(matrix)





"""
WHAT HAPPENS IF "SOM" INITIALIZATION IS FORGOTTEN ?
-> You get an error saying that Som isn't defined.

WHAT CAN YOU EXPECT IF ALL THE VALUES ARE BELLOW ZERO ?
-> If your values are bellow zero, you wont be able to access the average calculation since you're testing each 
values in the array are bellow zero. In the end, the function will attempt to divide 0 by 0 (default values), and throw
and error back.
"""

