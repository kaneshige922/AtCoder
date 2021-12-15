n = int(input())
s = [input() for i in range(n)]

ans = {}
for i in s[0]:
    if i in ans:
        ans[i] = ans[i] + 1
    else:
        ans[i] = 1
 
for i in s[1:]:
    k = {}
    for j in i:
        if j in k:
            k[j] = k[j] + 1
        else:
            k[j] = 1
    p = []
    for j in ans:
        if j in k:
            ans[j] = min(ans[j],k[j])
        else:
            p.append(j)
    for j in p:
        del ans[j]

kotae = []
for i in ans:
    for j in range(ans[i]):
        kotae.append(i)

kotae.sort()

print("".join(kotae))
