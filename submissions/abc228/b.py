
n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 1

fri = x-1
v = set([x-1])

while(1):
    if a[fri]-1 not in v:
        ans += 1
        fri = a[fri]-1
        v.add(fri)
    else:
        break

print(ans)
