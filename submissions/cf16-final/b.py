n = int(input())


while n!=0:
    left = 0
    right = n
    mid = (left+right)//2
    while right-left>1:
        if n <= mid*(mid+1)//2:
            right = mid
        else:
            left = mid
        mid = (right+left)//2
    print(right)
    n -= right
