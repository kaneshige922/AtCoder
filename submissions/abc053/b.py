import math

n = int(input())
a = list(map(int,input().split()))

cnt = 0
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
        if dic[i] >= 2:
            cnt += 1
    else:
        dic[i] = 1



print(n-math.ceil(cnt/2)*2)
