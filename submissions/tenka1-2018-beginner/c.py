n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()


l = 0
r = n-1

dif = []

for i in range(n-1):
    dif.append(a[r]-a[l])
    if i % 2 == 0:
        l += 1
        if i == n-2:
            dif.append(a[r]-a[0])
    else:
        r -= 1
        if i == n-2:
            dif.append(a[l]-a[0])


l = 0
r = n-1

dif2 = []
for i in range(n-1):
    dif2.append(a[r]-a[l])
    if i % 2 == 1:
        l += 1
        if i == n-2:
            dif2.append(a[n-1]-a[r])
    else:
        r -= 1
        if i == n-2:
            dif2.append(a[n-1]-a[l])

#print(dif)
#print(dif2)
dif.sort()
dif2.sort()

print(max(sum(dif)-dif[0],sum(dif2)-dif2[0]))
