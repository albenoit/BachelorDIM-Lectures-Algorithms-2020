# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import cv2
from random import *

def average(tab):
    
    '''
    
    This funtion calculates the average of a list
    
    Args : 
        tab: The list of number
        
    Returns the mean of the list
    
    Raises:
        Value error if no positive value is find
    '''
    
    som = 0
    n=0
    for i in range(len(tab)):
        if tab[i] > 0:
            som = som + tab[i]
            n = n+1
    if n>0:
        moy = som/n
    else:
        raise ValueError('no positive value found')
    return(moy)
    
    '''
    What happens if som initilization is forgotten ?
        L'erreur NameError: name 'som' is not defined
        Il faut donc la déclarer
        
    What can you expect if all the values are below zero ?
        Le calcul ne les prendra pas en compte  
    '''
    
def max_value(tab):
    
    '''
    
    This function returns the maximum value of a list
    
    Args :
        tab: The list of number
        
    Returns the maximum value of the list given
    
    '''
    
    max=tab[0]
    for i in tab:
        if i >= max:
            max=i
    return(max)
    
def reverse_table(tab):
    '''
    
    This function returns the reverse of the input table
    
    Args :
        tab: input table
        
    Returns the inverted table
    
    '''
    listlen=len(tab)
    for i in range (len(tab)//2):
        tmp=tab[i]
        endid=listlen-i-1
        tab[i]=tab[endid]
        tab[endid]=tmp
    #tab=tab[::-1]
    return(tab)


boolean_matrix=np.zeros((12,10),dtype=bool)
for c in range (7,9):
    for l in range (4,9):
        boolean_matrix[l,c]=1


def roi_bbox(array):
    '''
    This function returns a numpy array of shape 4x2 filled with the four 2D coordinates
    
    Args:
        lx, ly : Gives x and y coordinates of non null values
        coordinates: np.array that contains coordinates of the object
    Returns a numpy array of shape 4x2 filled with the four 2D coordinates
    '''
    lx, ly = np.nonzero(array)
    if lx is None or ly is None:
        raise ValueError("no non null value found")
    else:
        coordinates=np.array([
                [np.min(lx),np.min(ly)],
                [np.max(lx),np.max(ly)]
                ])
    return(coordinates)
    
char_matrix_empty=np.empty([10,10],dtype=str)


def random_fill_sparse(matrice,k):
    '''
    This function fills randomly an empty str np array of X
    
    Args :
        matrice: Empty np array of str type
        k : int corresponding to the number of X that will be placed in matrice
    '''
    
    xmax=len(matrice)
    ymax=len(matrice[1])
    for loop in range(k):
        x,y=randint(0,xmax-1),randint(0,ymax-1)
        matrice[x,y]='X'
    return matrice

def remove_whitespace(string):
    '''
    This function remove whitespaces from a string
    
    Args :
        string: input string that you have to treate
        
    Raises :
        TypeError : string is str type only
    '''
    
    return(string.replace(' ',''))
    
    
"""

/!\ This is just a test to try cv2 library

test=cv2.imread('test.jpg',0)
test1=cv2.imread('test.jpg',1)
cv2.imshow("test",test)
cv2.imshow("test1",test1)
cv2.waitKey()

"""

def invert_color_manual(imgpath):
    
    ''' 
    This function invert the color of the input image path. This ain't optimized for python and very long to apply.
    
    Args :
        imgpath: input path of the image you want to convert
        
    Returns the negative of the image
    '''

    get_picture=cv2.imread(imgpath)
 
    
    out_picture=np.zeros(get_picture.shape, dtype=np.uint8)
    
    for row in range (get_picture.shape[0]):
        for col in range (get_picture.shape[1]):
            for channel in range (get_picture.shape[2]):
                out_picture[row,col,channel]=255-get_picture[row,col,channel]
    
    return out_picture


def invert_color_numpy(img):
    ''' 
    This function invert the color of the input image. This is kind of optimized for python.
    
    Args :
        img: input image you want to convert
    
    Returns the negative of the image
    '''
    if img is None:
        raise ValueError('expected an uint8 nd array')
    if not (isinstance(img,np.ndarray)):
        raise TypeError('expected nd array')
    if img.dtype!=np.dtype(np.uint8):
        raise TypeError('expected uint8 typed nd aray')
    
    return 255-img

def invert_color_opencv(img):
    ''' 
    This function invert the color of the input image. This is kind of optimized for python.
    
    Args :
        img: input image you want to convert
    
    Returns the negative of the image
    '''
    return cv2.bitwise_not(img,1)
   
   
   
