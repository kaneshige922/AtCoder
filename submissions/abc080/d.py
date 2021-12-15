


n,C = map(int,input().split())
stc = [list(map(int,input().split())) for i in range(n)]

cnt = [0 for i in range(10**5+2)]
cnt2 = [[set(),set()] for i in range(C+1)]



for s,t,c in stc:
    if  t in cnt2[c][0]:
        cnt[t-1] -= 1
    else:
        cnt[t] -= 1
    if s in cnt2[c][1]:
        cnt[s] += 1
    else:
        cnt[s-1] += 1
    
    cnt2[c][0].add(s)
    cnt2[c][1].add(t)

#print(cnt[:20])

import itertools 
def ruisekiwa(a):
    return list(itertools.accumulate(a))

cnt = ruisekiwa(cnt)


print(max(cnt))
