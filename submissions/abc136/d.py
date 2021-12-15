import math

s = input()
r = [0]
l = []
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        if s[i] == "L":
            l.append(i)
        else:
            r.append(i)
r.append(len(s))

ans = [0]*len(s)

for i in range(len(l)):
    ans[l[i]] += math.ceil((r[i+1]-l[i])/2) + math.floor((l[i]-r[i])/2)
    ans[l[i]-1] += r[i+1]-r[i] - ans[l[i]]

print(*ans)
