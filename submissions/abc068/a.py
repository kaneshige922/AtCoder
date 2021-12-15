n,m = map(int,input().split())

ship = [[] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    ship[a-1].append(b-1)
    ship[b-1].append(a-1)
ship1 = [set(ship[i]) for i in range(n)]

for i in range(len(ship[0])):
    if n-1 in ship1[ship[0][i]]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE") 
