tab = [1,2,11,4,5,6,16,8,9]

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

print(get_index_max_value(tab))