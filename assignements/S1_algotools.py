list = [12, 14, 16, 17, 18]

def average_above_zero(table:list):
    '''
        This function calculate the average of a list 
        Parameters:
            table: List of number
        Returns:
            the average
        Raises:
            Value error if no positive value n
    '''
    som=1
    n=0
    for i in range(1, len(table)):
        if table[i] > 0:
            som = som + table[i]
            n = n + 1
    if n > 0:
        Moy = som/n
        return print(float(Moy))
    else:
        raise ValueError('no positive value n')

average_above_zero(list)

# What happens if Som initialization is forgotten ?

# On a le message d'erreur: NameError: name 'som' is not defined. 
# Celle-ci signifie que la variable som n'est pas défini avant d'etre utilisé 


# What can you expect if all the values are below zero ?

#  On a le message d'erreur: ZeroDivisionError: division by zero
# Cela arrive quand l'on ne rentre pas dans la condition p_list[i] > 0 et donc que n reste nulle 


def max_value(table:list):
    '''
        This function search the maximum value of a list
        Parameters:
            table: List of number
        Returns:
            the maximum value of a list
    '''
    max_nb=0
    max_id=0
    for i in range(1, len(table)):
        if table[i] > 0 and table[i] > max_nb:
            max_nb = table[i] 
            max_id = i
    return print(float(max_nb),int(max_id))


max_value(list)


def reverse_table(table:list):
    '''
        This function reverse a list
        Parameters:
            table: List of number
        Returns:
            a reverse list
    '''
    return print(table[:: -1])


reverse_table(list)

import numpy as np
H=15
W=15
Xin = np.zeros((H,W),dtype=float)
Xin[6:7,8:9]=np.ones((1,1))
for c in range(7,10):
    for l in range(7,10):
        Xin[l,c]=1

def roi_bbox(img): 
    '''
        This function return boundingbox
        Parameters:
            img: Binary image
        Returns:
            boundingBox in numby array
    '''
    (x,y)=img.shape
    x1=x;y1=x;x2=0;y2=0
    # check=1
    for c in range(0,x):
        for l in range(0,y):
            if img[c,l]==1:
                    # x1=l
                    # y1=c
                    # check=0
                # elif img[c,l]==1 and check==0:
                    # x2=l
                    # y2=c
                if l<x1:
                    x1=l
                if c<y1:
                    y1=c
                if l>x2:
                    x2=l
                if c>y2:
                    y2=c
    return np.array([x1,y1,x2,y2])
print(Xin)
print(roi_bbox(Xin))
    
chaine = "Kentucky Fried Chicken"
def remove_whitespace(string):
    '''
        This function paste the words 
        Parameters:
            string: sentence
        Returns:
            the sentence without wthitespace
    '''
    ChaineF = ""
    for i in string:
        if i != ' ':
            ChaineF+=i
    return ChaineF
print(remove_whitespace(chaine))

import random 
def shuffle(list_in:list):
    '''
        This function mix the value of a list
        Parameters:
            list_in: List of number
        Returns:
            a shuffle list
    '''
    for i in range(len(list_in)-1, 0, -1): 
        j = random.randint(0, i + 1)  
        list_in[i], list_in[j] = list_in[j], list_in[i]  

    return list_in

list=[1, 4, 5, 6, 3] 
print(shuffle(list))