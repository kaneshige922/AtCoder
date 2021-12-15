a,b = map(int,input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

ay = set(prime_factorize(a))
by = set(prime_factorize(b))

ans = 1

for i in ay:
    if i in by:
        ans += 1

print(ans)
