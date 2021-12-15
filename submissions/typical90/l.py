n,q = map(int,input().split())
a = list(map(int,input().split()))

dif = [a[i+1]-a[i] for i in range(n-1)]
score = sum([abs(i) for i in  dif])

for i in range(q):
    l,r,v = map(int,input().split())
    if l != 1:
        score += abs(dif[l-2]+v)-abs(dif[l-2])
        dif[l-2] = dif[l-2]+v
    if r != n:
        score += abs(dif[r-1]-v)-abs(dif[r-1])
        dif[r-1] = dif[r-1]-v
    print(score)    

