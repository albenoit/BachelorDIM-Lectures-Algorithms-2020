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
    if(len(table)):
        Som = 0
        positif_element = 0
        for tableValue in table:
            if(tableValue>0):
                Som += tableValue
                positif_element+=1
        if(positif_element>0):
            Moy = Som/positif_element
        else:
            raise ValueError('No value abrove zero in the list')
        return(Moy)
    else:
        raise ValueError('List is empty')

def max_value(table:list):
    '''
        This function find the max value on a number list
        
        Parameters:
            table:list: the list of number.            
        Returns: 
            the max number on table:list
    '''
    if(len(table)):
        Max = 0
        for tableValue in table:
            if(Max < tableValue):
                Max = tableValue
        return(Max)
    else:
        raise ValueError('List is empty')

def reverse_table(table:list):
    '''
        This function reverse a list
        Parameters:
            table:list: the list of number.            
        Returns: 
            reverse of table:list
    '''
    if(len(table)):
        table.reverse()
        return table
    else:
        raise ValueError('List is empty')

Tab=[0]   #To use list.reverse(), I have change () to []
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))
print("Liste avant : "+ str(Tab))
print("Liste après : "+ str(reverse_table(Tab)))