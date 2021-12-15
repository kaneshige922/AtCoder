n,k = map(int,input().split())
a = list(map(int,input().split()))

s = {}
count = 0

for i in a:
    if i in s:
        s[i] = s[i] + 1
    else:
        s[i] = 1
        count += 1

num = []

for i in s:
    num.append(s[i])

num.sort()

if len(num) <= k:
    print(0)
else:
    ans = sum(num[:(len(num)-k)])
    print(ans)
