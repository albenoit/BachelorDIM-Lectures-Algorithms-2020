"""
Created by Yoan ROULEAU
@author: myself
"""

Tab = [-6, 1, 2]

def average_above_zero(array):
    '''
    Receives an array as a parameter and calculates its average.

    :arg
        array: an array
    :returns
        moy: Its average
    '''
    som = 0
    n = 0
    for i in array:
        if i > 0:
            som = som + i
            n += 1
        else:
            raise ValueError('No positive values found in the array.')
    if n > 0:
        moy = som/n

    return float(moy)


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
    return array[::-1]


print('Average: ' + str(average_above_zero(Tab)))
print('Max: ' + str(max_value(Tab)))
print('Reverse: ' + str(reverse_table(Tab)))


"""
WHAT HAPPENS IF "SOM" INITIALIZATION IS FORGOTTEN ?
-> You get an error saying that Som isn't defined.

WHAT CAN YOU EXPECT IF ALL THE VALUES ARE BELLOW ZERO ?
-> If your values are bellow zero, you wont be able to access the average calculation since you're testing each 
values in the array are bellow zero. In the end, the function will attempt to divide 0 by 0 (default values), and throw
and error back.
"""

