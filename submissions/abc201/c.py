s = list(input())

ans = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                V = set([a,b,c,d])
                t = True
                for i in range(10):
                    if s[i] == "o" and i not in V:
                        t = False
                    elif s[i] == "x" and i in V:
                        t = False
                if t:
                    ans += 1

print(ans)
