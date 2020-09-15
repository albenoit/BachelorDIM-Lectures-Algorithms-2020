"""
Created by Yoan ROULEAU
@author: myself
"""

Som=0
N=0
Tab = [1, 2]
for i in Tab:
    if i > 0:
        Som = Som + i
        N = N + 1
Moy = Som/N
print(Moy)

#WHAT HAPPENS IF "SOM" INITIALIZATION IS FORGOTTEN ?
#-> You get an error saying that Som isn't defined.

