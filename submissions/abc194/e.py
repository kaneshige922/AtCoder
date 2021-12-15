
n,m = map(int,input().split())
a = list(map(int,input().split()))

v = []

dic = {}
ok = [1]*(n+1)

for i in range(m):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
        ok[a[i]] = 0


for i in range(1,n-m+1):
    if a[i-1] != a[i+m-1]:
        dic[a[i-1]] -= 1
        if dic[a[i-1]] == 0:
            ok[a[i-1]] = 1
        if a[i+m-1] in dic:
            dic[a[i+m-1]] += 1
        else:
            dic[a[i+m-1]] = 1

#print(ok)
for i in range(n+1):
    if ok[i]:
        print(i)
        exit()
