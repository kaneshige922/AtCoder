from collections import deque

n = int(input())
s = deque(list(input()))

ans = deque()
l = []
cnt = 0

while s:
    h = s.popleft()
    if h == ")":
        ans.append(h)
        if cnt == 0:
            ans.appendleft("(")
        else:
            cnt -= 1
    else:
        ans.append(h)
        cnt += 1

for i in range(cnt):
    ans.append(")")

print("".join(ans))
