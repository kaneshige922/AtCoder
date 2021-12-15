
s1 = [input() for i in range(2)]

ans = set()

for i in range(2):
    for j in range(2):
        if s1[i][j] == "#":
            ans.add((i,j))

ans = list(ans)

if len(list(ans)) >= 3:
    print("Yes")
elif abs(ans[0][0]-ans[1][0]) == 1 and abs(ans[0][1]-ans[1][1]) == 1:
    print("No")
else:
    print("Yes")
