x,n = map(int,input().split())
if n != 0:
    p = list(map(int,input().split()))
else:
    print(x)
    exit()
p.sort()
set(p)
mini = 100
ans = 100
if p[n-1]< x:
    print(x)
elif p[0] > x:
    print(x)
else:
    for i in range(102):
        if not(i in p):
            if abs(x-i) < mini:
                mini = abs(x-i)
                ans  = i
    print(ans)
