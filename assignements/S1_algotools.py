import numpy as np

def average_above_zero(tab :list):
    '''
    Function to add average of positive numbers in array
    This function add one array of numbers in args
    Parameters :
        tab: array of numbers in input
    Returns :
        the average of positive numbers
    '''
    som=0 #Sum of positive numbers in array. Init at 0
    N=0 #Count of positive numbers in array. Init at 0
    
    for i in range(len(tab)):
        if tab[i] > 0: # If number is > 0
            som += tab[i]
            N += 1
    
    # Calculate the average if positive numbers find
    if N > 0:
        average = som / N
    else:
        raise ValueError('No positive number found')

    return average # Return average

# Call the function with array in args and display the average
# print('# Average above zero function # ')
# print('T1 : average = ' , average_above_zero([1,10,2,8,12])) #Only positive numbers
# print('T2 : average = ' , average_above_zero([1,-10,-2,-8,12])) #With positive and negative numbers
# print('T3 : average = ' , average_above_zero([-1,-10,-2,-8,-12])) #Only negative numbers

def max_value(tab :list):
    '''
    Function to get the number with the max value in array
    Parameters :
        tab: array of numbers in input
    Returns :
        the index of max value numbers
        the max number
    '''
    maxNumber = max(tab) # Get the max number in tab
    maxNumberIndex = tab.index(maxNumber) # Get index of max number
    return maxNumberIndex, maxNumber # Return index of max number & the max number

# Call the function with array in args and display the index of max value
# print('# Max value index function #')
# print('T1 = ', max_value([1,10,2,8,11])) #Only positive numbers
# print('T2 = ', max_value([1,10,2,8,-11])) #With positive and negative numbers
# print('T3 = ', max_value([-1,-10,-2,-8,-11])) #Only negative numbers

# Reverse table V1
def reverse_table(tab :list):
    '''
    Function to reverse and return a reversed array
    Parameters :
        tab: array of numbers in input
    Returns :
        the reversed array
    '''
    tab = list(reversed(tab))

    return tab

# Call the function with array in args and display reversed array
# print('# Reverse table function #')
# print(reverse_table([1,10,2,8,11]))

# Reverse table V2
def reverse_table_V2(tab : list):
    '''
    Function to reverse and return a reversed array
    Parameters :
        tab: array of numbers in input
    Returns :
        the reversed array
    '''
    for i in range(-1, -len(tab) - 1, -1):
        n = tab[i]
        tab.pop(i)
        tab.append(n)
    return tab

# Call the function with array in args and display reversed array 
# print('# Reverse table function V2 #')
# print(reverse_table_V2([1,10,2,8,11]))

# Reverse table V3
def reverse_table_V3(tab : list):
    '''
    Function to reverse and return a reversed array
    Parameters :
        tab: array of numbers in input
    Returns :
        the reversed array
    '''
    listen = len(tab)
    for i in range(len(tab)//2):
        n = tab[i]
        tab[i] = tab[listen-i-1]
        tab[listen-i-1] = n
    return tab

# Call the function with array in args and display reversed array 
# print('# Reverse table function V3 #')
# print(reverse_table_V3([1,10,2,8,11]))



# Bounding box
def run():
    H=12
    W=10
    matrix=np.zeros((H,W))
    # matrix[2:3, 3:5]= np.ones((2,2)) * 2
    for c in range(1,3):
        for l in range(3,5):
            matrix[l,c] = 1
    for c in range(5,8):
        for l in range(6,9):
            matrix[l,c] = 1
# print(matrix)

if __name__ ==  "__main__":
    run()

def roi_bbox(img):
    '''
    Function to get coordinates of img in matrix
    Parameters :
        img: matrix of img
    Returns :
        the coordinates of img
    '''
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    targets = np.argwhere(img > 0)
    # print(targets)

    x1 = targets[0][0]
    y1 = targets[0][1]
    x2 = targets[len(targets) - 1][0]
    y2 = targets[len(targets) - 1][1]
    return(np.array([x1, y1, x2, y2]))

# Call the function with matrix in args and display img coordinates
# print('# Bounding box function V1 #')
# print('T1 : img coordinate = ',roi_bbox(matrix))

def roi_bbox_V2(img):
    '''
    Function to get coordinates of img in matrix V2
    Parameters :
        img: matrix of img
    Returns :
        the coordinates of img
    '''
    W = img.shape[0] - 1
    H = img.shape[1] - 1
    x1 = W
    y1 = H
    x2 = 0
    y2 = 0
    for x in range(0,W):
        for y in range(0,H):
            # print(x,y)
            if img[x,y]:
                if x < x1:
                    x1 = x
                if y < y1:
                    y1 = y 
                if y > y2:
                    y2 = y
                if x > x2:
                    x2 = x
    return(np.array([x1, y1, x2, y2]))

# Call the function with matrix in args and display img coordinates
# print('# Bounding box function V2 #')
# print('T2 : img coordinate = ',roi_bbox_V2(matrix))


# Random array filling
import random

RandomArray = np.zeros((10,10))
K = 200
# print(RandomArray)

def random_fill_sparse(matrix, k):
    '''
    Function to insert X values in random cells of matrix
    Parameters :
        matrix: matrix of where insert X values
        k: numbers of cells
    Returns :
        a np.array with X values inserted
    '''
    randomList = []
    maxRandomNumber = (matrix.shape[0]) * (matrix.shape[1])
    if k > maxRandomNumber:
        raise ValueError('Too randoms numbers will be create')

    # print(maxRandomNumber)
# Set a length of the list to 10
# for i in range(0, k):
#     # any random numbers from 0 to 1000
#     randomList.append(random.randint(0, 1000))

# print("Printing list of 10 random numbers")
# print(randomList)

