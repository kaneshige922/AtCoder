from collections import deque

n = int(input())
s = input()


qu = deque(["z","z"])

ans = n

for i in range(n):
    if s[i] == "f":
        qu.append(s[i])
    elif s[i] == "o":
        if qu[-1] == "f":
            qu.append(s[i])
        else:
            qu = deque(["z","z"])
    elif s[i] == "x":
        if qu[-1] == "o" and qu[-2] == "f":
            qu.pop()
            qu.pop()
            ans -= 3
        else:
            qu = deque(["z","z"])
    else:
        qu = deque(["z","z"])

print(ans)
