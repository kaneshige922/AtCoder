from collections import deque
#import pprint

a = [list(input()) for i in range(10)]
ans = [[0]*10 for i in range(10)]



q = deque()
v = set()
to = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
for i in range(10):
    for j in range(10):
        if a[i][j] == "o" and tuple([i,j]) not in v:
            cnt += 1
            q.append(tuple([i,j]))
            v.add(tuple([i,j]))
            v2 = set()
            v2.add(tuple([i,j]))
            while q:
                h = q.popleft()
                for k in to:
                    x = h[0] + k[0]
                    y = h[1] + k[1]
                    if (0 <= x and x <10) and (0 <= y and y < 10):
                        if a[x][y] == "x":
                            if tuple([x,y]) not in v2:
                                ans[x][y] += 1
                                v2.add(tuple([x,y]))
                        else:
                            if tuple([x,y]) not in v:
                                q.append(tuple([x,y]))
                                v.add(tuple([x,y]))

for i in range(10):
    for j in range(10):
        if ans[i][j] == cnt:
            print("YES")
            #pprint.pprint(ans)
            #print(cnt)
            exit()

print("NO")
#pprint.pprint(ans)

