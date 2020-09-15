tab = [1,2,3,4,5,6,7,8,9]

def max_value(tab):
    """function max_value(tab)
    
    return maximum value of list 'tab'
    """
    max_val = 0

    for i in tab:
        if i > max_val:
            max_val = i

    return max_val

print(max_value(tab))