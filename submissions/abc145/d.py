import sys
sys.setrecursionlimit(1000000)


x,y = map(int,input().split())

"""""
def saiki(a,b):
    if a==0 and b==0:
        return 1
    elif abs(a+b)<=2:
        return 0
    else:
        return saiki(a-2,b-1)+saiki(a-1,b-2)%mod
"""
#print(saiki(x,y))

if (x+y)%3 != 0:
    print(0)
    exit()

a = (2*y-x)//3
b = (2*x-y)//3

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N ‚Í•K—v•ª‚¾‚¯—pˆÓ‚·‚é
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = cmb(a+b,b,p)

print(ans)
