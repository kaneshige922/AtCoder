n,x = map(int,input().split())
X = list(map(int,input().split()))

X1 = [abs(i-x) for i in X]

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b,r)


if n == 1:
    print(abs(X[0]-x))
    exit()


g = gcd(X1[0],X1[1])
if n >= 3:
    for i in range(2,n):
        g = gcd(g,X1[i])

print(g)
