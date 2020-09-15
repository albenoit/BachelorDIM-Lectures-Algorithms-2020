list = [12, 14, 16, 17, 18]

def average_above_zero(table:list):
    '''
        This function calculate the average of a list 
        Parameters:
            table: List of number
        Returns:
            the average
    '''
    som=1
    n=0
    for i in range(1, len(table)):
        if table[i] > 0:
            som = som + table[i]
            n = n + 1
    Moy = som/n
    return print(float(Moy))

average_above_zero(list)

# What happens if Som initialization is forgotten ?

# On a le message d'erreur: NameError: name 'som' is not defined. 
# Celle-ci signifie que la variable som n'est pas défini avant d'etre utilisé 


# What can you expect if all the values are below zero ?

#  On a le message d'erreur: ZeroDivisionError: division by zero
# Cela arrive quand l'on ne rentre pas dans la condition p_list[i] > 0 et donc que n reste nulle 


def max_value(table:list):
    '''
        This function search the maximum value of a table
        Parameters:
            table: List of number
        Returns:
            the maximum value of a table
    '''
    max_nb=0
    max_id=0
    for i in range(1, len(table)):
        if table[i] > 0 and table[i] > max_nb:
            max_nb = table[i] 
            max_id = i
    return print(float(max_nb),int(max_id))


max_value(list)


