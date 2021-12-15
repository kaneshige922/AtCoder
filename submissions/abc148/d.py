n = int(input())
a = list(map(int,input().split()))

s = 1
for i in a:
    if i == s:
        s += 1

if s != 1:
    print(n-s+1)
else:
    print(-1)
