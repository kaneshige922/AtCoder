n =int(input())
v = list(map(int,input().split()))
v1 = [v[2*i] for i in range(n//2)]
v2 = [v[2*i+1] for i in range(n//2)]

d1 = {}
d2 = {}

for i in range(n//2):
    if v1[i] in d1:
        d1[v1[i]] += 1
    else:
        d1[v1[i]] = 1
    if v2[i] in d2:
        d2[v2[i]] += 1
    else:
        d2[v2[i]] = 1
d1_sort = sorted(d1.items(),reverse = True,key=lambda x:x[1])
d2_sort = sorted(d2.items(),reverse = True,key=lambda x:x[1])

if d1_sort[0][0] != d2_sort[0][0]:
    print(n-d1_sort[0][1]-d2_sort[0][1])
elif len(d1_sort) == 1 and len(d2_sort) == 1:
    print(n//2)
else:
    a = n-d1_sort[0][1]-d2_sort[1][1]
    b = n-d1_sort[1][1]-d2_sort[0][1]
    print(min(a,b))
