s = list(input())

mark = ""

cnt = 0
ans = 0

for i in range(len(s)-2):
    if s[i] == s[i+1] and s[i+1] != s[i+2] and mark != s[i]:
        #print(s[i])
        ans += cnt
        mark = s[i]
        cnt = len(s)-i-2
    elif s[i+2] == mark:
        cnt -= 1
ans += cnt

print(ans)
