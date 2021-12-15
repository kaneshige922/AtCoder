import math

n =int(input())
csf = [list(map(int,input().split())) for i in range(n-1)]

for i in range(n-1):
    t = csf[i][0] + csf[i][1]
    for j in range(i+1,n-1):
        if t <= csf[j][1]:
            t = csf[j][0]+csf[j][1]
        else:
            t = math.ceil(t/csf[j][2])*csf[j][2] + csf[j][0]
    print(t)
print(0)
 
