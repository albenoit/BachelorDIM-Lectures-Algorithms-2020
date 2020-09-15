som=0
n=0
p_list=10,12,15,8,16
for i in range(1, len(p_list)) :
    if (p_list[i] > 0):
        som = som + p_list[i]
        n = n + 1
moy = som/n
print(moy)