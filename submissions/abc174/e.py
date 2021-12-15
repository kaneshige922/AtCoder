import math

n,k = map(int,input().split())
a = list(map(int,input().split()))

#Œˆ‚ß‘Å‚¿“ñ•”’Tõ

left = 0
right = 1000000000
mid = (left+right)//2

while right-left>1:
    cnt = 0
    for i in range(n):
        cnt += math.ceil(a[i]/mid)-1
    if cnt <= k:
        right = mid
    else:
        left = mid
    mid = (right+left)//2

print(right)
