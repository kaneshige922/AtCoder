n = int(input())
a = list(map(int,input().split()))

ans = [0]*n
for i in range(n):
    ans[a[i]-1] = i+1

ans = [str(i) for i in ans]

print(" ".join(ans))
