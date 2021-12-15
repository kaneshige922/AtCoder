k = int(input())

def gcd(a,b):
    m = min(a,b)
    glis = []
    for i in range(1,m+1):
        if a%i == 0 and b%i == 0:
            glis.append(i)
    glis.reverse()
    return  glis

def gcd2(a,b):
    g = 1
    for i in a:
        if b % i == 0:
            g = i
            break
    return g

ans = 0

for i in range(1,k+1):
    for j in range(1,k+1):
        koyaku = gcd(i,j) 
        for k in range(1,k+1):
            ans += gcd2(koyaku,k)
            
            
print(ans)
