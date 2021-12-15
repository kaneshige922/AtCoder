h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
t = [[]for i in range(h)]
t2 = [[]for i in range(w)]
for i in range(h):
    cnt = 0
    for j in range(w):
        if s[i][j] == ".":
            cnt += 1
            if j == w-1:
                for k in range(cnt):
                    t[i].append(cnt)
        else:
            for k in range(cnt):
                t[i].append(cnt)
            t[i].append(0)
            cnt = 0
for i in range(w):
    cnt = 0
    for j in range(h):
        if s[j][i] == ".":
            cnt += 1
            if j == h-1:
                for k in range(cnt):
                    t2[i].append(cnt)
        else:
            for k in range(cnt):
                t2[i].append(cnt)
            t2[i].append(0)
            cnt = 0


ans = 0

for i in range(h):
    for j in range(w):
        ans = max(ans,t[i][j]+t2[j][i]-1)

print(ans)

