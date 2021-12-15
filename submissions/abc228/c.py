
n,k = map(int,input().split())


score = []
score2 = []
for i in range(n):
    a,b,c = map(int,input().split())
    score.append(a+b+c)
    score2.append(a+b+c)

score2.sort(reverse=True)

lower = score2[k-1]-300

for i in score:
    if i < lower:
        print("No")
    else:
        print("Yes")
