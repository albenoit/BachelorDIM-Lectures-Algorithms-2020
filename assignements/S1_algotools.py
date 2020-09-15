def average_above_zero(tab):
    '''
    Function to add average of positive numbers in array
    This function add one array of numbers in args
    Parameters :
        tab: array of numbers
    Returns :
        the average of positive numbers
    '''
    som=0 #Sum of positive numbers in array. Init at 0
    N=0 #Count of positive numbers in array. Init at 0
    
    for i in range(len(tab)):
        if tab[i] > 0: # If number is > 0
            som = som + tab[i]
            N = N + 1
    
    # Calculate the average
    average = som / N

    return average # Return average

# Call the function with array in args
print('Average : ')
print(average_above_zero([1,10,2,8,-2]))

