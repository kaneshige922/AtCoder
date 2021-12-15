n = int(input())

if n % 2 != 0:
    print(0)
    exit()

ans = 0

n2 = n//2

k = 5

while(k<=n2):
    ans += n2//k
    k *= 5


print(ans)
