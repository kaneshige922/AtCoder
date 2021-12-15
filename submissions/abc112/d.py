n,m = map(int,input().split())

def yakusu(n):
    import math
    ylist = []
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i == n//i:
                ylist.append(i)
            else:
                ylist.append(i)
                ylist.append(n//i)
    ylist.sort()
    return ylist

    
    
y = yakusu(m)

ans = 1
for i in y:
    if m//i >= n:
        ans = i

print(ans)
