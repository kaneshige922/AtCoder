n,s,d = map(int,input().split())
zyumon = []
for i in range(n):
    zyumon.append(list(map(int,input().split())))

ans = False

for i in range(n):
    if zyumon[i][0] < s and zyumon[i][1] > d:
        ans = True
        break
if ans:
    print("Yes")
else:
    print("No")
