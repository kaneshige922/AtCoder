import math

n = int(input())

ans = []

for i in range(1,math.floor(math.sqrt(n))+1):
    if n % i == 0:
        ans.append(i)
        if i != n//i:
            ans.append(n//i)

ans.sort()
for i in ans:
    print(i)
