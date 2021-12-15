n = int(input())
a = list(map(int,input().split()))

import itertools 
def ruisekiwa(a):
    return list(itertools.accumulate(a))

ac = ruisekiwa(a)

flag = True #•„†ŠÇ—@True:+

def Cost(flag):
    dif = 0
    cnt = 0

    for j in ac:
        i = j
        i += dif
        if flag and i <= 0:
            cnt += 1-i
            dif += 1-i
        elif not(flag) and i >= 0:
            cnt += i+1
            dif -= i+1
        flag = not(flag)
    return cnt

ans = min(Cost(True),Cost(False))

print(ans)
