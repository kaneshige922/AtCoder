from decimal import *

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int,input().split())))

xy.sort()

s = set()

for i in range(n-1):
    for j in range(i+1,n):
        if xy[j][0]-xy[i][0] != 0:
            #ss = (xy[j][1]-xy[i][1])/(xy[j][0]-xy[i][0])
            ss = (Decimal(xy[j][1]-xy[i][1]))/Decimal(xy[j][0]-xy[i][0])
        else:
            ss = float("inf")
        #print(ss)
        s.add(ss)

s = list(s)


print(len(s)*2)
