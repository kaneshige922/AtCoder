import math

d,g = map(int,input().split())
pc = [list(map(int,input().split())) for i in range(d)]

all = [100*(i+1)*pc[i][0] + pc[i][1] for i in range(d)]

ans = float("inf")

for i in range(2**d):
    n = g
    cnt = 0
    ma = -1
    for j in range(d):
        if (i >> j) & 1:
            n -= all[j] 
            cnt += pc[j][0]
        else:
            ma = j
    if n > 0  and ma != -1:
        #print(min(math.ceil(n/(100*(ma+1))),pc[ma][0]-1))
        cnt += min(math.ceil(n/(100*(ma+1))),pc[ma][0]-1)
        n -= min(math.ceil(n/(100*(ma+1))),pc[ma][0]-1)*100*(ma+1)
    if n <= 0:
        ans = min(cnt,ans)


print(ans)

            






