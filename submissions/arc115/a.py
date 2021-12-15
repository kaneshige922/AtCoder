n,m = map(int,input().split())
s = [input() for i in range(n)]


ans = [[0],[]]

for i in range(1,n):
    cnt = 0
    for j in range(m):
        if s[0][j] != s[i][j]:
            cnt += 1
    ans[cnt%2].append(i)

print(len(ans[0])*len(ans[1]))    
    
