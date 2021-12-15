from copy import deepcopy

n = int(input())
a = list(map(int,input().split()))
dic = {}
ma = max(a)
for i in a:
    j = deepcopy(i)
    cnt = 1
    while j <= ma:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
        cnt += 1
        j = i*cnt

ans = 0

for i in a:
    if dic[i] == 1:
        ans += 1

print(ans)
