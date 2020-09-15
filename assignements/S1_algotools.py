def average_above_zero(table:list):
    '''
    This function calculate the average of a list of numbers
    
    Parameters :
        list : the list of numbers
    
    Return : 
        the average of the list

    Raises : 
        Value error if no positive value in the division
    '''
    som=0
    n=0
    for i in range(1, len(table)) :
        if (table[i] > 0):
            som = som + table[i]
            n = n + 1
        else:
            raise ValueError('No positive value in the division')
    moy = som/n
    return print(moy)

# list = [8, 15, 14, 12, 6, 18, 10, 2, 20]
# average_above_zero(list)

# What happens if Som initialization is forgotten ?
# On a une erreur qui nous dit que Som n'est pas défini NameError: name 'som' is not defined

# What can you expect if all the values are below zero ?
# On a un message d'erreur qui nous dit qu'on ne peut pas diviser par 0 : ZeroDivisionError: division by zero
# Et on vérifie ça avec le if (p_list[i] > 0):

def get_maximum_value(table:list):
    '''
    This function found the max value of a list of numbers
    
    Parameters :
        list : the list of numbers
    
    Return : 
        the max value of a list and the position
    '''
    max=0
    rg=0
    for i in range(1, len(table)):
        if table[i] > 0 and table[i] > max:
            max = table[i]
            rg = i
    return print(float(max), int(rg))

# list = [8, 15, 14, 12, 6, 18, 10, 2]
# get_maximum_value(list)

def reverse_table(table:list):
    '''
    This function reverse a table
    Parameters :
        list : the list of numbers
    
    Return : 
        the table reverse
    '''

    return print(table[:: -1])

list = [8, 15, 14, 12, 6, 18, 10, 2]
reverse_table(list)