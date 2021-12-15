n,k = map(int,input().split())

ab = [list(map(int,input().split())) for i in range(n)]

ab.sort()

cnt = 0

for a,b in ab:
    cnt += b
    if cnt >= k:
        print(a)
        exit()
