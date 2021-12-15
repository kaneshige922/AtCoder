h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

ans = [[0 for i in range(w+2)] for j in range(h+1)]

acnt = 1
cnt = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        if i % 2 != 0:
            ans[i][j] = acnt
            cnt += 1
            if a[acnt-1] == cnt:
                acnt += 1
                cnt = 0
        else:
            ans[i][-j-1] = acnt 
            cnt += 1
            if a[acnt-1] == cnt:
                acnt += 1
                cnt = 0

for i in range(1,h+1):
    print(*ans[i][1:w+1])



