tab = [1,9,3,4,5,6,7,8,2]

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

def max_value(tab):
    """function max_value(tab)
    
    return maximum value of list 'tab'
    """
    max_val = 0

    for i in tab:
        if i > max_val:
            max_val = i

    return max_val

def get_index_max_value(tab):
    """function get_index_max_value(tab)
    
    return index of maximum value of list 'tab'
    """
    max_val = 0
    n = 0
    index = 0

    for i in tab:
        n+=1
        if i > max_val:
            max_val = i
            index = n

    return index

def reverse_table(tab):
    """function reverse_table(tab)
    
    return reverse of list 'tab'
    """
    return tab[::-1]

print(average_above_zero(tab))
print(max_value(tab))
print(get_index_max_value(tab))
print(reverse_table(tab))