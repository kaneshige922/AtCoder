n = int(input())
a = list(map(int,input().split()))
c1 = 0
c2 = 0
c4 = 0

for i in range(n):
    if a[i] % 4 == 0:
        c4 += 1
    elif a[i] % 2 == 0:
        c2 += 1
    else:
        c1 += 1

if c2 == 0:
    if n // 2 <= c4:
        print("Yes")
    else:
        print("No")
else:
    if c1 <= c4:
        print("Yes")
    else:
        print("No")
