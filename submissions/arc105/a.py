a = list(map(int,input().split()))

k = sum(a)

for i in range(2**4):
    eat = 0
    nkr = k
    for j in range(4):
        if i >> j & 1:
            eat += a[j]
            nkr -= a[j]
    if eat == nkr:
        print("Yes") 
        exit()

print("No")
