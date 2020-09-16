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
print('# Max value index function #')
print('T1 = ', max_value([1,10,2,8,11])) #Only positive numbers
print('T2 = ', max_value([1,10,2,8,-11])) #With positive and negative numbers
print('T3 = ', max_value([-1,-10,-2,-8,-11])) #Only negative numbers

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
print('# Reverse table function #')
print(reverse_table([1,10,2,8,11]))

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
print('# Reverse table function V2 #')
print(reverse_table_V2([1,10,2,8,11]))


