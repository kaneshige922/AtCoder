n = int(input())

abc = [list(map(int,input().split())) for i in range(n)]

malist = [0,0,0,0,0]

for i in range(n):
    for j in range(5):
        malist[j] = max(malist[j],abc[i][j])
        

ans = 0

for i in range(n):
    for j in range(i,n):
        score = [0,0,0,0,0]
        mi = -1
        mi1 = 10**9
        for k in range(5):
            score[k] = max(abc[i][k],abc[j][k])
            if score[k] < mi1:
                mi1 = score[k]
                mi = k
        score[mi] = malist[mi]
        ans = max(ans,min(score))

print(ans)
