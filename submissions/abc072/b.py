n = int(input())
p = list(map(int,input().split()))

ans = 0
t = True
for i in range(n):   
    if p[i] == i+1:
        if t:
            ans += 1
            t = False
        else:
            t = True
    else:
        t = True

print(ans)
