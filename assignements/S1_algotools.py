def average_above_zero(table:list):
    som=1
    n=0
    for i in range(1, len(table)):
        if table[i] > 0:
            som = som + table[i]
            n = n + 1
    Moy = som/n
    return Moy

list = [12, 14, 16, 17, 18]
print(average_above_zero(list))
# What happens if Som initialization is forgotten ?

# On a le message d'erreur: NameError: name 'som' is not defined. 
# Celle-ci signifie que la variable som n'est pas défini avant d'etre utilisé 


# What can you expect if all the values are below zero ?

#  On a le message d'erreur: ZeroDivisionError: division by zero
# Cela arrive quand l'on ne rentre pas dans la condition p_list[i] > 0 et donc que n reste nulle 
