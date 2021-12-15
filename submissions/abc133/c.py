l,r = map(int,input().split())

if r - l >= 2019 or r % 2019 < l % 2019:
    print(0)
    exit()
modl = l % 2019
modr = r % 2019

ans = 2019

for i in range(modl,modr):
    for j in range(i+1,modr+1):
        mod = (i*j)%2019
        ans = min(ans,mod)

print(ans)
