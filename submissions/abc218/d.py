n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]

x = set()
y = set()
point = set()

for i in xy:

    point.add(tuple(i))



ans = 0


for i in point:
    for j in point:
        if i[0]!=j[0] and i[1]!=j[1]:
            if tuple([i[0],j[1]]) in point and tuple([j[0],i[1]]) in point:
                ans += 1

print(ans//4)
