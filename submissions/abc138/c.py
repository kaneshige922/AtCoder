n = int(input())
v = list(map(float,input().split()))
v.sort()

ans = 0

for i in range(n-1):
    new = (v[0]+v[1])/2
    v = v[2:]
    v.append(new)
    v.sort()

print(v[0])
