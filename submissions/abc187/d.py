n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
ab.sort(reverse=True,key=lambda x:2*x[0]+x[1])

ao = sum([ab[i][0] for i in range(n)])
tk = 0


for i in range(n):
    ao -= ab[i][0]
    tk += ab[i][0] + ab[i][1]
    if tk > ao:
        print(i+1)
        exit()
