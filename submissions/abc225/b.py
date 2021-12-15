
n = int(input())
dic = {}
for i in range(1,n+1):
    dic[i] = set()

for i in range(n-1):
    a,b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)

cnt = 0
for i in range(1,n+1):
    if len(list(dic[i])) == n-1:
        cnt += 1


if cnt == 1:
    print("Yes")
else:
    print("No")
