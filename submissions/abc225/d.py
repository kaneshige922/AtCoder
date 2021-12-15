from collections import deque

n,q = map(int,input().split())

z = [[-1,-1] for i in range(n+1)]


ans = []

for i in range(q):
    qu = list(map(int,input().split()))

    if qu[0] == 1:
        z[qu[1]][1] = qu[2]
        z[qu[2]][0] = qu[1]
    elif qu[0] == 2:
        z[qu[1]][1] = -1
        z[qu[2]][0] = -1
    else:
        l = deque()
        l.append(qu[1])
        h = qu[1]
        cnt = 1
        while(1):
            if  z[h][0] != -1:
                h = z[h][0]
                l.appendleft(h)
                cnt += 1
            else:
                break
        h = qu[1]
        while(1):
            if  z[h][1] != -1:
                h = z[h][1]
                l.append(h)
                cnt += 1
            else:
                break
        l.appendleft(cnt)
        ans.append(list(l))

for i in ans:
    print(*i)
