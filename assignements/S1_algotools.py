"""
Created by Yoan ROULEAU
@author: myself
"""

Tab = [1, 2, 3]

def getAverage(array):
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
            n = n + 1
    moy = som/n
    return moy

def getMax(array):
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

print('Average: ' + str(getAverage(Tab)))
print('Max: ' + str(getMax(Tab)))

"""
WHAT HAPPENS IF "SOM" INITIALIZATION IS FORGOTTEN ?
-> You get an error saying that Som isn't defined.

WHAT CAN YOU EXPECT IF ALL THE VALUES ARE BELLOW ZERO ?
-> If your values are bellow zero, you wont be able to access the average calculation since you're testing each 
values in the array are bellow zero. In the end, the function will attempt to divide 0 by 0 (default values), and throw
and error back.
"""

