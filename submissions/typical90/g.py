k = int(input())

ans = 0

for i in range(1,k+1):
    if i*i > k:
        break
    if k % i == 0:
        kk = k//i
        for j in range(i,kk+1):
            if j*j > kk:
                break
            if kk % j == 0 and kk //j >= j:
                ans += 1

print(ans)
