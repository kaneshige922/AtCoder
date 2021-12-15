n = int(input())
f = []
p = []
for i in range(n):
    f.append(list(map(int,input().split())))
for i in range(n):
    p.append(list(map(int,input().split())))

ans = -float("inf")

for i in range(1,2**10):
    cnt = [0]*n
    rie = 0
    for j in range(10):
        if (i >> j) & 1:
            for k in range(n):
                if f[k][j] == 1:
                    cnt[k] += 1
    for j in range(n):
        rie += p[j][cnt[j]]
    ans = max(ans,rie)

print(ans)
