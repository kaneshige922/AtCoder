
import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)

left = 0
right = n
mid = (left+right)//2

while(right-left>1):
    size = sum(a[mid:])
    #print(mid,size)
    t = True
    for i in range(mid):
        if a[mid-1-i] <= 2*size:
            size += a[mid-1-i]
        else:
            t = False
            break
    if(t):
        left = mid
    else:
        right = mid
    mid = (left+right)//2

print(left+1)
