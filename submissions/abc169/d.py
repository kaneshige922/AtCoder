n = int(input())

import collections 

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
#print(collections.Counter(prime_factorize(n)))

a = prime_factorize(n)

dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 0

for i in dic:
    t = dic[i]
    left = 0
    right = 1000
    mid = (left+right)//2
    while right-left > 1:
        if mid*(mid+1)//2 <= t:
            left = mid
        else:
            right = mid
        mid = (left+right)//2
    ans += left

print(ans)
