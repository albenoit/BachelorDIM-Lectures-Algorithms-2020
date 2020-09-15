som=0
n=0
p_list=[-10,-12,-15,-12,-16,-20]
for i in range(1, len(p_list)):
    if p_list[i] > 0:
        som = som + p_list[i]
        n = n + 1
Moy = som/n
print(Moy)

# What happens if Som initialization is forgotten ?

# On a le message d'erreur: NameError: name 'som' is not defined. 
# Celle-ci signifie que la variable som n'est pas défini avant d'etre utilisé 


# What can you expect if all the values are below zero ?

#  On a le message d'erreur: ZeroDivisionError: division by zero
# Cela arrive quand l'on ne rentre pas dans la condition p_list[i] > 0 et donc que n reste nulle 
