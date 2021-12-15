
s = list(input())
k = int(input())

Xma = 0
cnt = 0

dot = []

for i in range(len(s)):
    if s[i] == ".":
        dot.append(i+1)
        Xma = max(Xma,cnt)
        cnt = 0
    else:
        cnt += 1

Xma = max(Xma,cnt)

if k == 0:
    print(Xma)
    exit()


#print(dot)

if len(dot) <= k:
    print(len(s))
    exit()

#print(dot)




ans = dot[k-1]

for i in range(k,len(dot)-1):
    a = dot[i+1]-dot[i-k]-1
    ans = max(ans,a)

ans = max(ans,len(s)-dot[len(dot)-1-k])

print(ans)
