n = list(input())
n = [int(i) for i in n]
nlen = len(n)

ans = -1
for i in range(2**nlen):
    x = []
    y = []
    for j in range(nlen):
        if i>>j & 1:
            x.append(n[j])
        else:
            y.append(n[j])
    x.sort(reverse=True)
    y.sort(reverse=True)
    if len(x) > 0 and len(y) >0:
        x = int("".join([str(k) for k in x]))
        y = int("".join([str(k) for k in y]))
        ans = max(ans,x*y)

print(ans)
