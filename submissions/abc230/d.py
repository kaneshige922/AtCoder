
n,d = map(int,input().split())

LR = [list(map(int,input().split())) for i in range(n)]


LR.sort(key=lambda x:x[1])

#print(LR)

to  = 0
cnt = 0

for l,r in LR:
    if l <= to:
        continue
    cnt += 1
    to = r+d-1

print(cnt)    
