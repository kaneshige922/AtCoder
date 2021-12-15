n,m = map(int,input().split())
s = list(input())
s.reverse()
#print(s)
#dp = [0 for i in range(n+1)]


x = 0
cnt = 0
ans = []
while x < n:
    y = x
    if n-x <= m:
        ans.append(n-x)
        break
    for i in range(m):
        if s[x+m-i] == "0":
            x += m-i
            ans.append(m-i)
            break
    if x == y:
        print(-1)
        exit()
    #print(*ans,x)

ans.reverse()
print(*ans)




