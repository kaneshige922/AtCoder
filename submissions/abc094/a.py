n = int(input())
x = list(map(int,input().split()))
x1 = sorted(x)
xl = x1[n//2 -1]
xr = x1[n//2]

for i in x:
    if i <= xl:
        print(xr)
    else:
        print(xl)
