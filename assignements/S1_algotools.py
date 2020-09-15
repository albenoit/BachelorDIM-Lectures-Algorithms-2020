import numpy as np

tab = [1,9,3,4,5,6,7,8,2]

np_tab = np.array([
    [0,1,0],
    [1,1,1],
    [0,1,0]
])

def average_above_zero(tab):
    """
    This function calculate the average of list tab

    Parameters :
        tab: the list
    Returns :
        return the average of list
    """
    som = 0
    n = 0

    for i in tab:
        if i > 0:
            som += i
            n += 1

    return som / n

def max_value(tab):
    """
    This function determine the max value of list tab

    Parameters :
        tab: the list
    Returns :
        return the max value of list
    """
    max_val = 0

    for i in tab:
        if i > max_val:
            max_val = i

    return max_val

def get_index_max_value(tab):
    """This function determine the index of max value of list tab

    Parameters :
        tab: the list
    Returns :
        return the index of max value of list
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
    """
    This function reverse the table

    Parameters :
        tab: the list
    Returns :
        return the reverse table
    """
    return tab[::-1]

def bounding_box(np_tab):
    """
    This function determine coordinates of true values

    Parameters :
        np_tab: the numpy array
    Returns :
        return the coordinates of true values
    """
    return np.argwhere(np_tab == 1)

print(average_above_zero(tab))
print(max_value(tab))
print(get_index_max_value(tab))
print(reverse_table(tab))
print(bounding_box(np_tab))