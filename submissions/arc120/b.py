h,w = map(int,input().split())

s = [list(input()) for i in range(h)]
mod = 998244353

ans = 1

for i in  range(h+w-1):
    v = set()
    for x in range(h):
        y = i-x
        if 0<= y < w:
            v.add(s[x][y])
    if "R" in v and "B" in v:
        ans = 0
    elif "R" in v or "B" in v:
        pass
    else:
        ans *= 2
    ans %= mod

print(ans)
