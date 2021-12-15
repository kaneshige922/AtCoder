n = int(input())

ans = 0
for i in range(6):
    if n >= 10**(3*i):
        ans += i*(min(10**(3*(i+1))-1,n)-10**(3*i)+1)

print(ans)
