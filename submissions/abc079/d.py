#ダイクストラ

h,w = map(int,input().split())
c = [list(map(int,input().split())) for i in range(10)]
a = [list(map(int,input().split())) for i in range(h)]
kyori = []


for i in range(10):
    kyo = [float("inf") for p in range(10)]   
    kyo[i] = 0
    he = i
    v = set([he])
    while len(v) < 10:
        for k in range(10):
            if k not in v:
                kyo[k] = min(kyo[k],kyo[he]+c[he][k])
        tugi = -1
        cost = float("inf")
        for k in range(10):
            if (k not in v) and cost > kyo[k]:
                tugi = k
                cost = kyo[k]
        he = tugi
        v.add(he)
    kyori.append(kyo)
                    
ans = 0

for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += kyori[a[i][j]][1]


print(ans)
