n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]


ans = 0

for a in range(n-2):
    for b in range(a+1,n-1):
        for c in range(b+1,n):
            if (xy[b][1]-xy[a][1])*(xy[c][0]-xy[a][0]) != (xy[c][1]-xy[a][1])*(xy[b][0]-xy[a][0]):
                ans += 1

print(ans)
