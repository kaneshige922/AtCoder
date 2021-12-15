n = int(input())
xyh = [list(map(int,input().split())) for i in range(n)]




for c1 in range(101):
    for c2 in range(101):
        t = True
        h = -1
        for i in range(n):
            if xyh[i][2] != 0:
                h = xyh[i][2] + abs(xyh[i][0]-c1) + abs(xyh[i][1]-c2)
                break
        for i in range(n):
            if xyh[i][2] != max(h-abs(xyh[i][0]-c1)-abs(xyh[i][1]-c2),0):
                t = False
                break
        if t:
            print(c1,c2,h)
            break

