
n = int(input())
a = list(map(int,input().split()))

if a[0] != 0:
    print(0)
    exit()


cnt = [0]*n

for i in a:
    cnt[i] += 1

if cnt[0] > 1:
    print(0)
    exit()

MOD = 998244353
ans = [0]*n
ans = 1

for i in range(1,n):
    ans = (pow(cnt[i-1],cnt[i],MOD)*ans)%MOD

print(ans)

