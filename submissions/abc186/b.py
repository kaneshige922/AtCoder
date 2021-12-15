h,w = map(int,input().split())
block = []
bmin = 100
for i in range(h):
    a = list(map(int,input().split()))
    block.append(a)
    bmin = min(min(a),bmin)

ans = 0

for i in range(h):
    for j in range(w):
        ans += block[i][j] - bmin

print(ans)
