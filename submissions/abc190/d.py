n = int(input())

ans = 0
t = (2*n)**0.5
s = set()
for i in range(1,2*n):
    if i >= t:
        break
    if 2*n % i == 0:
        if i % 2 != ((2*n)//i) % 2:
            ans += 2

print(ans)
