
n,k = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(n)]
xy.sort()

#print(xy)

ans = float("inf")
"""""
for i in range(n-k+1):
    ymi = xy[i][1]
    yma = xy[i][1]
    for j in range(i+1,i+k):
        ymi = min(ymi,xy[j][1])
        yma = max(yma,xy[j][1])
    
    ans = min(ans,(xy[i+k-1][0]-xy[i][0])*(yma-ymi))

print(ans)
"""

#‘S’Tõ

for i in range(n-1):
    for j in range(i+1,n):
        for s in range(n-1):
            for t in range(s+1,n):
                x1 = xy[i][0]
                x2 = xy[j][0]
                y1 = min(xy[s][1],xy[t][1])
                y2 = max(xy[s][1],xy[t][1])
                cnt = 0
                for p in range(n):
                    if x1 <= xy[p][0] <= x2 and y1 <= xy[p][1] <= y2:
                        cnt += 1
                if cnt >= k:
                    ans = min(ans,(x2-x1)*(y2-y1))

print(ans)
