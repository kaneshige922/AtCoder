
n = int(input())
s = list(map(int,input().split()))


ans = n

for i in (s):
    t = False
    for a in range(1,1001):
        for b in range(1,1001):
            if 4*a*b+3*a+3*b == i:
                ans -= 1
                t = True
                break
        if t:
            break

print(ans)
        
            

