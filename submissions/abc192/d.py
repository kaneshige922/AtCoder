
X = input()
m = int(input())

d = 0
for i in X:
    d = max(d,int(i))

if len(X) == 1:
    if int(X) <= m:
        print(1)
    else:
        print(0)
    exit()

left = 1
right = m+1
mid = (left+right)//2

while right-left >1:
    x = 0
    for i in range(len(X)):
        x += (mid**i)*int(X[-(i+1)])
        if x > m:
            break
    if x <= m:
        left = mid
    else:
        right = mid
    mid = (left+right)//2

if left - d > 0:
    print(left-d)
else:
    print(0)
