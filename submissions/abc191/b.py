n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = []

for i in range(n):
    if x != a[i]:
        ans.append(a[i])
ans = [str(i) for i in ans]
print(" ".join(ans))
