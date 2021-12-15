n,m = map(int,input().split())
ms = list(map(int,input().split()))
ms.sort()
sa = []
if m <= n :
    print(0)
    exit()
for i in range(1,m):
    sa.append(ms[i]-ms[i-1])

sa.sort()

ans = sum(sa[:(m-n)])

print(ans)
