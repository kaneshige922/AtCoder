
n,m = map(int,input().split())
a = list(map(int,input().split()))

def yakusu(n):
    import math
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i <= m and i != 1:
                yak.add(i)
            if n//i <= m and n//i != 1:
                yak.add(n//i)
    
yak = set()
for i in a:
    yakusu(i)

ans = [True for i in range(m)]

for i in yak:
    for j in range(1,m+1):
        if i*j > m:
            break
        ans[i*j-1]=False

cnt = 0

for i in ans:
    if i:
        cnt += 1

print(cnt)
for i in range(m):
    if ans[i]:
        print(i+1)
