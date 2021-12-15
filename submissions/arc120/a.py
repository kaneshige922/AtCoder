import numpy as np

n = int(input())
a = list(map(int,input().split())) 
ac = np.cumsum(a)
ac = np.cumsum(ac)
mal = [a[0]]
for i in range(1,n):
    mal.append(max(mal[i-1],a[i]))
for i in range(n):
    print(ac[i]+mal[i]*(i+1))

