n = int(input())

n1 = n**0.5

masu = []

for i in range(1,n):
    if i > n1:
        break
    if n % i == 0:
        j = n //i
        masu.append([i,j])
        masu.append([j,i])

ans = 10**12
for i in masu:
    hosu = i[0]+i[1]-2
    ans = min(ans,hosu)

print(ans)
