tab = [1,2,3,4,5,6,7,8,9]

def average_above_zero(tab):
    """function average_above_zero(tab)
    
    return average of list 'tab'
    """
    som = 0
    n = 0

    for i in tab:
        if i > 0:
            som += i
            n += 1

    return som / n

print(average_above_zero(tab))

"""
1- If Som isn't initalized, program throw error (NameError) because 
   we're using it in loop.

2- Throw error because n will be equal to 0 and we're splitting som by n (x/0)

3- /

4- /
"""