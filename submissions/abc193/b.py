n = int(input())
store = []
for i in range(n):
    store.append(list(map(int,input().split())))

ans = 10**9
pur = False

for i in range(n):
    if store[i][0] < store[i][2] and store[i][1] < ans:
        ans = store[i][1]
        pur = True

if pur:
    print(ans)
else:
    print(-1)
