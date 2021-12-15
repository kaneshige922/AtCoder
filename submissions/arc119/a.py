n = int(input())


ans = float("inf")

for i in range(60):
    j = 2**i
    if j <= n:
        a = i + n//j + n%j
        ans = min(a,ans)
    else:
        break

print(ans)
