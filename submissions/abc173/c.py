h,w,k = map(int,input().split())
c = []
for i in range(h):
    c.append(list(input()))

ans = 0

for i in range(2**h):
    bin(i)
    for j in range(2**w):
        bin(j)
        count = 0
        for n in range(h):
            if (i >> n) & 1: 
                for m in range(w):
                    if (j >> m) & 1:
                        if c[n][m] == "#":
                            count += 1 
        if count == k:
            ans += 1

print(ans)
