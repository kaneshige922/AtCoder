def myceil(a,b):
    return a//b + (a%b!=0)


n = int(input())
lr = [list(map(int,input().split())) for i in range(n)]

if n == 1:
    print(0)
    exit()

Lmin = min(lr[0][0],lr[1][0])
Rmin = min(lr[0][1],lr[1][1])
Lma = max(lr[0][0],lr[1][0])
Rma = max(lr[0][1],lr[1][1])
print(0)
if Lma > Rmin:
    print(myceil(Lma-Rmin,2))
else:
    print(0)
    

for i in range(2,n):
    l = lr[i][0]
    r = lr[i][1]
    Lmin = min(Lmin,l)
    Rmin = min(Rmin,r)
    Lma = max(Lma,l)
    Rma = max(Rma,r)
    if Lma > Rmin:
        print(myceil(Lma-Rmin,2))
    else:
        print(0)

