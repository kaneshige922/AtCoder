n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

ab.reverse()

cnt = 0

for a,b in ab:
    if (a+cnt)%b != 0:
        cnt += b-(a+cnt)%b

print(cnt)
