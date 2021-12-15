n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

wl = [False for i in range(n)]

ans = 0

for i in range(n):
    if i <= k-1:
        if t[i] == "r":
            ans += p
        elif t[i] == "s":
            ans += r
        else:
            ans += s
        wl[i] = True
    else:
        if t[i] == t[i-k]:
            if not(wl[i-k]):
                if t[i] == "r":
                    ans += p
                elif t[i] == "s":
                    ans += r
                else:
                    ans += s
                wl[i] = True
        else:
            if t[i] == "r":
                ans += p
            elif t[i] == "s":
                ans += r
            else:
                ans += s
            wl[i] = True

print(ans)
