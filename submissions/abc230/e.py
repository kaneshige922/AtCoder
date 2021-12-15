
N = int(input())

t = 1


left = 1
right = N+1
mid = (left+right)//2
before = N+1
ans = 0

while (t!=N):
    while(right-left > 1):
        k = N//mid
        if k <= t:
            right = mid
        else:
            left = mid
        mid = (left+right)//2

    ans += (before-right)*(N//right)
    t = N//left
    #print(right,before,t)
    before = right
    left = 1
    mid = (left+right)//2


ans += N
print(ans)


