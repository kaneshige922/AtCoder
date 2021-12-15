from collections import deque

import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

s = input()

t = deque()

flag = False

for i in s:
    if i == "R":
        flag = not(flag)
    else:
        if len(t) != 0:
            if flag:
                if i == t[0]:
                    t.popleft()
                else:
                    t.appendleft(i)
            else:
                if i == t[-1]:
                    t.pop()
                else:
                    t.append(i)
        else:
            t.append(i)

t = "".join(list(t))
if flag:
    t = t[::-1]

print(t)

