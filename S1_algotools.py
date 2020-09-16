from random import *
import numpy as np
'''
a=1
b='e'+a
'''

'''//////////////////////////////////////////////////'''

def average_above_zero(table:list):
 '''
 This function return the average of a table given in parameters
 Args : 
     table : the list        
 Returns : the average of the list
 '''
 som = 0
 n = 0
 i = 0
 for i in range(len(table)):
     if len(table) > 0 :
         som = som + (table[i])
         n = n + 1
 return som/n
 
  
'''//////////////////////////////////////////////////'''


def max_value(table:list):
 '''
 This function return the max of a table given in parameters
 Args : 
     table : the list        
 Returns : the max value of the list
 '''
 vmax = 0
 for i in range(len(table)):
     if len(table) > 0 :
         if vmax < (table[i]):
             vmax = (table[i])
 return vmax
 
'''//////////////////////////////////////////////////'''

def reverse_table(table:list):
 '''
 This function return the reverese form of a table given in parameters
 Args : 
     table : the list        
 Returns :  value of the list
 '''
 i = 0
 j = len(table)  - 1
 
 for i in range(int((j+1)/2)):
     permut = table[i]
     table[i] = table[j]
     table[j] = permut
     i = i+1
     j= j-1
 return table

'''//////////////////////////////////////////////////'''

def roi_bbox(input_image: np.array):
 '''
 This function return the reverese form of a table given in parameters
 Args : 
     table : the list        
 Returns   
 ''' 
 stop = 0
 '''coin haut gauche'''
 for i in range(len(input_image)):
  for j in range(len(input_image[0])):
      if input_image[i,j] > 0:
       CHG = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break

 stop = 0
   
 print("///////////////////")
 
 '''coin haut droit'''
 for i in range(len(input_image)):
  for j in reversed(range(len(input_image[0]))):
      if input_image[i,j] > 0:
       CHD = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break
 stop = 0
 print("///////////////////")
 
 '''coin bas droit'''
 for i in reversed(range(len(input_image))):
  for j in reversed(range(len(input_image[0]))):
      if input_image[i,j] > 0:
       CBD = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break
 stop = 0
       
 print("///////////////////")
 
 '''coin bas droit'''
 for i in reversed(range(len(input_image))):
  for j in range(len(input_image[0])):
      if input_image[i,j] > 0:
       CBG = i + 1, j+ 1 
       stop = 1
       break
  if stop == 1:
   break
 stop = 0

 print (CHG,CHD,CBG,CBD)
 
 '''bounding_box = 0
 if CHG[0] < CBD[0]:
  bounding_box = str(CHG) + " " + str(CBD)
  print(bounding_box)
 if CHG[0] > CBD[0]: 
  bounding_box = str(CHD) + " " + str(CBG)
  print(bounding_box)
 ''' 
  
 if CHG[1] < CBD[1]:
      newCHD = CHG[0],CBD[1]
      newCBG = CBG[0],CHG[1]
      
 print(CHG,newCHD,newCBG,CBD)     
 '''
      x1>x   x1 = 0
      y<y1   y1 =y
      x2 < x x2 = x
      y2 < y y2=y
  '''
 return input_image

def alea(v:int):
 return randint(1,v)  
    

def random_array_filling(table:np.array,k:int):
 malist = []
 for i in range(k):
  x = alea(len(table) - 1)
  y = alea(len(table[0]) - 1)
  print(malist)
  if (x,y) in malist:
      print("doublon")
      i = i -1
  else:
    table[x,y] = alea(100) 
  malist.insert(0,(x,y))  

 position = np.argwhere(table)
 print(len(position))    
 return table
  

maTable = [1,2,3,4]
print(reverse_table(maTable))
'''print(max_value(maTable))'''
'''print(average_above_zero(maTable))'''
'''
H = 12
W = 10
monImage = np.zeros((H,W))
monImage[8:10,7:9] = np.ones((2,2))
monImage[2:4,3:5] = np.ones((2,2))*2
print(roi_bbox(monImage))'''
maMatriceChar = np.zeros((10,10))
'''print(random_array_filling(maMatriceChar,10))'''

