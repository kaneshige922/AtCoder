n = int(input())
a = list(map(int,input().split()))

ans = 0

for i in a:
    for j in range(1,30):
        if i % 2**j == 0:
            ans += 1 

print(ans)
