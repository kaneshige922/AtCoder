n = int(input())
a = list(map(int,input().split()))
aa = [abs(i) for i in a]
a.sort()
aa.sort()
tasu = 0
hiku = 0
zero = 0
for i in a:
    if i < 0:
        hiku += 1
    elif i > 0:
        tasu += 1
    else:
        zero += 1

if (2*n-hiku)%2 == 0 or zero != 0:
    ans = sum(aa)
else:
    ans = sum(aa) - 2*aa[0]

print(ans)
