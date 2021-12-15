n = int(input())
s = [list(input()) for i in range(n)]
s = [sorted(s[i]) for i in range(n)]
s = [str(s[i]) for i in range(n)]
slis = {}

for i in range(n):
    if s[i] in slis:
        slis[s[i]] = slis[s[i]] + 1
    else:
        slis[s[i]] = 1

ans = 0
for i in slis.values():
    ans +=  i*(i-1)

print(ans//2)
