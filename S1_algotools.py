# -*- coding: utf-8 -*-

def average_above_zero(table:list):
    '''
        This function calcul average from number list
        Only number above zero is add to the average
        
        Parameters:
            table:list: the list of number .
        Returns: 
            the average of table:list
    '''
    Som = 0
    positif_element = 0
    for tableValue in table:
        if(tableValue>0):
            Som += tableValue
            positif_element+=1
    if(positif_element>0):
        Moy = Som/positif_element
    else:
        raise ValueError('no value greater than 0 in the list')
    return(Moy)

def max_value(table:list):
    '''
        This function find the max value on a number list
        
        Parameters:
            table:list: the list of number.            
        Returns: 
            the max number on table:list
    '''
    Max = 0
    for tableValue in table:
        if(Max < tableValue):
            Max = tableValue
    return(Max)

def reverse_table(table:list):
    '''
        This function reverse a list
        Parameters:
            table:list: the list of number.            
        Returns: 
            reverse of table:list
    '''
    table.reverse()
    return table

Tab=[-10,-21,-32,-43]   #To use list.reverse(), I have change () to []
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))
print("Liste avant : "+ str(Tab))
print("Liste après : "+ str(reverse_table(Tab)))