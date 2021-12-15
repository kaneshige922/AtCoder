n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]

ab.sort(key=lambda x:x[1])

t = 0
for i in ab:
    t += i[0]
    if t > i[1]:
        print("No")
        exit()

print("Yes")
