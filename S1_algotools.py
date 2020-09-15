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
    for tableValue in table:
        if(tableValue > 0):
            Som = Som + tableValue
    Moy = Som/len(table)
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
    
Tab=(10,21,32,43)
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))