n = int(input())
a = list(map(int,input().split()))

dic = {}
ans = 0

for i in range(n):
    x = i+1 - a[i]
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for i in range(n):
    if a[i] + (i+1) in dic:
        ans += dic[a[i] + (i+1)]

print(ans)
