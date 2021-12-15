import math

n = int(input())

ans = 1
dic = {}
for i in range(2,n+1):
    v = i
    while v % 2 == 0:
        if 2 in dic:
            dic[2] += 1
        else:
            dic[2] = 1
        v //= 2
    f = 3
    while f * f <= v:
        if v % f == 0:
            if f in dic:
                dic[f] += 1
            else:
                dic[f] = 1
            v //= f
        else:
            f += 2
    if v != 1:
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1

ans = 1

for i in dic.values():
    ans *= i+1

print(ans%1000000007)
