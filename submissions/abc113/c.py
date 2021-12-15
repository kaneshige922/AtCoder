n,m = map(int,input().split())
py = [list(map(int,input().split())) for i in range(m)]
py2 = sorted(py,key=lambda x:x[1])
zyun = [0]*n
dic = {}

for i in range(m):
    zyun[py2[i][0]-1] += 1
    dic[tuple(py2[i])] = zyun[py2[i][0]-1]

for i in py:
    s = str(i[0]).zfill(6)
    t = str(dic[tuple(i)]).zfill(6)
    print(s+t)

