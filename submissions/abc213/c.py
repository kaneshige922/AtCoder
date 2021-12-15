from bisect import bisect_left

h,w,n = map(int,input().split())

xset = set()
yset = set()
p = []
for i in range(n):
    a,b = map(int,input().split())
    p.append([a,b])
    xset.add(a)
    yset.add(b)

xset = sorted(list(xset))
yset = sorted(list(yset))

for i in p:
    print(bisect_left(xset,i[0])+1,bisect_left(yset,i[1])+1)
