n,m,q = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(n)]
wv.sort()
x = list(map(int,input().split()))
qu = [list(map(int,input().split())) for i in range(q)]


for i in range(q):
    l = qu[i][0]-1;r = qu[i][1]-1
    xl = []
    if l != 0:
        xl += x[:l]
    if r != m-1:
        xl += x[r+1:]
    xl.sort()
    ans = 0
    v = set()
    for j in xl:
        value = -1
        point = -1
        for k in range(n):
            if wv[k][0] <= j and wv[k][1] >= value and k not in v:
                value = wv[k][1]
                point = k
        if value != -1:
            ans += value
            v.add(point)
    print(ans)


