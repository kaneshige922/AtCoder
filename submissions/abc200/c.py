n = int(input())
A = list(map(int,input().split()))
AA = [i % 200 for i in A]
counta = [0 for i in range(200)]

ans = 0

for i in AA:
    counta[i] += 1
for i in counta:
    ans += int(i*(i-1)/2)
print(ans)
