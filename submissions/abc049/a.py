from collections import deque

s = input()

slen = len(s)

q = deque([0])
v = set([0])

ans = False

lis = ["dream","dreamer","erase","eraser"]

while q:
    l = q.popleft()
    for i in lis:
        tolen = len(i)
        if l+len(i) not in v:
            if i == s[l:l+len(i)]:
                q.append(l+len(i))
                v.add(l+len(i))
                if l+len(i) == slen:
                    ans = True
                    q.clear()
                    break


if ans:
    print("YES")
else:
    print("NO")


