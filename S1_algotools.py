from random import *
import numpy as np
import string
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
 '''
 print (CHG,CHD,CBG,CBD)
 '''
 if CHG[1] < CBD[1]:
      newCHD = CHG[0],CBD[1]
      newCBG = CBG[0],CHG[1]
 myResult = np.zeros((4,2))   
 myResult[0,0] = CHG[0]
 myResult[0,1] = CHG[1]
 myResult[1,0] = newCHD[0]
 myResult[1,1] = newCHD[1]
 myResult[2,0] = newCBG[0]
 myResult[2,1] = newCBG[1]
 myResult[3,0] = CBD[0]
 myResult[3,1] = CBD[1]

 '''
      x1>x   x1 = 0
      y<y1   y1 =y
      x2 < x x2 = x
      y2 < y y2=y
  '''
 return myResult

def alea(v:int):
 return randint(1,v)  
    

def random_array_filling(table:np.array,k:int):
 malist = []
 i = 1
 while i <= k:
  x = alea(len(table) - 1)
  y = alea(len(table[0]) - 1)
  
  if (x,y) in malist:
      '''print("doublon")'''
  else:
    table[x,y] = alea(100) 
    i = i + 1
  malist.insert(0,(x,y))
  

 
   
 return table

def remove_whitespace(table: string) :
 table = list(table) #transformation string -> table
 i = 0
 k = len(table)
 while i < k :
     if (table[i] == " ") :
           del table[i]
           k = k -1
           i = i -1
     i = i +1
        
 return "".join(table) #reconversion en string
     
def shuffle(list_in:list) :  
   for i in range(len(list_in) -1,0,-1) :
       maValeur = list_in[i]
       
       IndexEchange = randint(0,i)
       ValeurEchange = list_in[IndexEchange]
       
       if IndexEchange != i:
           list_in[i],list_in[IndexEchange] = ValeurEchange,maValeur
   return list_in
    
maTable = [1,2,3,4]
'''print(reverse_table(maTable))'''
'''print(max_value(maTable))'''
'''print(average_above_zero(maTable))'''

#H = 12
#W = 10
#monImage = np.zeros((H,W))
#monImage[8:10,7:9] = np.ones((2,2))
#monImage[2:4,3:5] = np.ones((2,2))*2
'''print(roi_bbox(monImage))'''
#maMatriceChar = np.zeros((10,10))
#print(random_array_filling(maMatriceChar,10))

#print(remove_whitespace("te     s t"));
print(shuffle(maTable))

