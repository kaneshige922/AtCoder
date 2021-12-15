n = int(input())
a = list(map(int,input().split()))

import itertools 
def ruisekiwa(a):
    return list(itertools.accumulate(a))

aa = ruisekiwa(a)

ans = 0
dic = {}
dic[0] = 1

for i in range(n):
    if aa[i] in dic:
        ans += dic[aa[i]]
    if aa[i] in dic:
        dic[aa[i]] += 1
    else:
        dic[aa[i]] = 1

print(ans)

