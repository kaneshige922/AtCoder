n = int(input())
a = list(map(int,input().split()))

g = a[0]
g1 = a[0]
pair = True

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b,r)

D = [i for i in range(10**6+1)]
def erto(n):
    Prime = [1]*(n+1) 
    for i in range(3,n+1):
        if i % 2 == 0:
            D[i] = 2
    y = 3
    while(y*y <= n):
        for i in range(y*y,n+1,y):
            if Prime[i]:
                D[i] = y
                Prime[i] = 0
        while(y*y <= n):
            y += 2
            if Prime[y]:
                break

def sb(x):
    global pair
    v = set()
    while(x!=1):
        v.add(D[x])
        x //= D[x]
    return list(v)

erto(10**6)
s = set()

for i in a:
    w = sb(i)
    for j in w:
        if j in s:
            pair = False
        else:
            s.add(j)    

#setwise”»’è
for i in a[1:]:
    g = gcd(g,i)

if pair:
    print("pairwise coprime")
elif g == 1:
    print("setwise coprime")
else:
    print("not coprime")
