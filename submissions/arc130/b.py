
H,W,C,Q = map(int,input().split())
qu = [list(map(int,input().split())) for i in range(Q)]
qu.reverse()

HV = set() # t==1
WV = set()
hcnt = 0
wcnt = 0

ans = [0 for i in range(C)]


for t,n,c in qu:
    if t == 1:
        if n not in HV:
            ans[c-1] += W - wcnt
            HV.add(n)
            hcnt += 1
    else:
        if n not in WV:
            ans[c-1] += H - hcnt
            WV.add(n)
            wcnt += 1

print(*ans)
