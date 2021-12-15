n = int(input())
a = list(map(int,input().split()))

b = [0 for i in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n//(n-i)-1):
        cnt += b[(n-i)*(j+2)-1]
    if cnt % 2 == a[n-i-1]:
        b[n-i-1] = 0
    else:
        b[n-i-1] = 1

ans = []

for i in range(n):
    if b[i] == 1:
        ans.append(i+1)

print(sum(b))
print(*ans)

        
