n = int(input())
c = list(input())

cnt = 0
for i in c:
    if i == "R":
        cnt += 1 

ans = cnt

for i in range(cnt):
    if c[i] == "R":
        ans -= 1

print(ans)

