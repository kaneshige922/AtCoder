n = int(input())
a = list(map(int,input().split()))

dic = {}

for i in a:
    for j in range(-1,2):
        if i+j not in dic:
            dic[i+j] = 1
        else:
            dic[i+j] += 1

ans = 0

for i in dic:
    ans = max(dic[i],ans)

print(ans)
