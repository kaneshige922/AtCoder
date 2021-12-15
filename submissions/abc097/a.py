s = input()
k = int(input())
t = set(list(s))
ch = []
for i in range(97, 123):
    ch.append(chr(i))


ans = []
cnt = 0
for i in ch:
    if i in t:
        ans.append(i)
        for j in range(len(s)):
            if s[j] == i:
                for l in range(1,k):
                    if j+l < len(s):
                        ans.append(s[j:j+1+l])
        ans = set(ans)
        ans = list(ans)
    if len(ans) >= k:
        break

ans.sort()
print(ans[k-1])
