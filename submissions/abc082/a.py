n = int(input())
a = list(map(int,input().split()))

s = {}
ans = 0
for i in a:
    if i in s:
        if s[i] < i:
              s[i] = s[i] + 1
        else:
            ans+=1
    else:
        s[i] = 1
for i in s:
    if i > s[i]:
        ans += s[i]


print(ans)
