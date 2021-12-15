a,b = map(int,input().split())

al = []
bl = []

if a <= b:
    for i in range(1,b+1):
        bl.append(-i)
        if i <= a:
            al.append(i)
        else:
            al[-1] += i
else:
    for i in range(1,a+1):
        al.append(i)
        if i <= b:
            bl.append(-i)
        else:
            bl[-1] -= i

ans = al+bl

print(*ans)

