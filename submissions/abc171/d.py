n = int(input())
a = list(map(int,input().split()))
q = int(input())
bc = [list(map(int,input().split())) for i in range(q)]

dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = sum(a)

for i in bc:
    if i[0] in dic:
        ans += (i[1]-i[0])*dic[i[0]]
        h = dic[i[0]]
        dic[i[0]] = 0
        if i[1] in dic:
            dic[i[1]] += h
        else:
            dic[i[1]] = h
    print(ans)
