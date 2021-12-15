
n,k = map(int,input().split())
kcnt = k
num = [n]
v = set([n])

t = True

for i in range(k):
    ns = str(n)
    for j in range(len(ns)):
        n += int(ns[j])
    n %= 10**5
    if n in v:
        t = False
    v.add(n)
    num.append(n)
    kcnt -= 1
    if not(t):
        break

roopn = 0
state = []

for i in range(len(num)):
    if num[i] == n:
        roopn = i - roopn
        state.append(i)


ans = num[kcnt%roopn+state[0]]

print(ans)
