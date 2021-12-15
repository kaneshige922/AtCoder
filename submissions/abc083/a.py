import math

x,y = map(int,input().split())

ans = 1

for i in range(60):
    if x*(2**(i+1)) <= y:
        ans += 1
    else:
        print(ans)
        exit()
