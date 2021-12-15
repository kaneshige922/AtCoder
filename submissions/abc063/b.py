def myceil(a,b):
    return a//b + (a%b!=0)


n,a,b = map(int,input().split())
h = [int(input()) for i in range(n)]


left = 0
right = 10**9
mid = (left+right)//2

while right-left > 1:
    B = b*mid
    cnt = 0
    for i in h:
        cnt += max(0,myceil(i-B,a-b))
    if cnt <= mid:
        right = mid
    else:
        left = mid
    mid = (left+right)//2

print(right)
