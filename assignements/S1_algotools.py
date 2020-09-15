# Average
def average(tab):
    """
    Calculate the average of a list
    Parameters
        tab
    Returns the average of the list
    """
    som = 0
    n = 0
    for i in range(len(tab)):
        if tab[i] > 0:
            som = som + tab[i]
            n = n + 1
    moy = som / n
    print(moy)


average([100, 20, 30])


# Maximum value
def max_value_in_tab(tab):
    """
    Get the maximum value of a tab
    Parameters
        tab
    Returns the maximum value of a tab
    """
    max = tab[0]
    for a in tab:
        if a > max:
            max = a
    return max


print(max_value_in_tab([1, 12, -8, 300]))


# Reverse a table
tab = [100, 'abc', 437, 'def', 123]
tab.reverse()
print(tab)







