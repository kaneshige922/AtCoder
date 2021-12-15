import math

n = int(input())


def prime_factorize(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            cnt += 1
            n //= f
        else:
            f += 2
    if n != 1:
        cnt += 1
    return cnt 

ans = prime_factorize(n)

if ans == 1:
    print(0)
else:
    a = 0
    while ans != 1:
        a += 1
        ans = math.ceil(ans/2)
    print(a)
