s = list(input())
ans = [s[0]]
for i in range(1,len(s)):
    if len(ans) >= 1:
        if ans[-1] != s[i]:
            ans.pop(-1)
        else:
            ans.append(s[i])
    else:
        ans.append(s[i])
    

print(len(s)-len(ans))
