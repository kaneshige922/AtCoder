n,m = map(int,input().split())
ab = []
for i in range(m):
    ab.append(list(map(int,input().split())))
k = int(input())
kl = []
for i in range(k):
    kl.append(list(map(int,input().split())))
    
ans = -1
    
for i in range(2**k):
    bin(i)
    c = [False]*n
    count = 0
    for j in range(k):
        if (i >> j) & 1:
            c[kl[j][1]-1] = True
        else:
            c[kl[j][0]-1] = True
    for j in range(m):
        if c[ab[j][0]-1] and c[ab[j][1]-1]:
            count += 1
    ans = max(ans,count)
print(ans)
