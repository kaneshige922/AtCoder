h,w = map(int,input().split())
P = [list(map(int,input().split())) for i in range(h)]

ans = 0

for i in range(1,2**h):
    gyo = []
    for j in range(h):
        if i >> j & 1:
            gyo.append(j)
    dic = {}
    for j in range(w):
        t = True
        for k in range(len(gyo)-1):
            if P[gyo[k]][j] != P[gyo[k+1]][j]:
                t = False
                break
        if t:
            if P[gyo[0]][j] in dic:
                dic[P[gyo[0]][j]] += 1
            else:
                dic[P[gyo[0]][j]] = 1
    if len(dic) != 0:
        ans = max(ans,len(gyo)*max(dic.values()))


print(ans)

