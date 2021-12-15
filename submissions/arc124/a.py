n,k = map(int,input().split())
ck = [list(input().split()) for i in range(k)]

a =  [0]*n
r = [0]*n
j = 1
for i in ck:
    if i[0] == "R":
        a[int(i[1])-1] = j
        r[int(i[1])-1] += 1
    else:
        a[int(i[1])-1] = j
        r[0] += 1
        r[int(i[1])-1] -= 1

for i in range(1,n):
    r[i] = r[i] + r[i-1]

ans = 1
kake = []
for i in range(n):
    if a[i] == 0:
        ans *= k-r[i]
        kake.append(k-r[i])

print(ans % 998244353)
