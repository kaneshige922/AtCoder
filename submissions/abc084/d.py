import numpy as np

q = int(input())
lr = [list(map(int,input().split())) for i in range(q)] 

def erto (x):
    x1 = x **0.5 
    sosu = [i+1 for i in range(x)]
    for i in range(2,x):
        if sosu[i] % 2== 0:
            sosu[i] = 0
    y = 3
    while y**2 < x:
        for j in range(y+1,x):
            if sosu[j] % y == 0:
                sosu[j] = 0
        t = True
        while t and y**2<x:
            y += 2
            if sosu[y-1] != 0:
                t = False
    sosu=set(sosu)
    sosu = list(sosu)
    return sosu[2:]

ss = set(erto(10**5))

ko = [0]*(10**5+1)

for i in range(1,10**5+1):
    if i in ss:
        if (i+1) //2 in ss:
            ko[i] = 1

ko = np.cumsum(ko)

for i in lr:
    print(ko[i[1]]-ko[i[0]-1])


