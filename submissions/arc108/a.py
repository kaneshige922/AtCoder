s,p = map(int,input().split())

import math
n = p
ylist = []
for i in range(1,math.floor(math.sqrt(n))+1):
    if n % i == 0:
        if i + n//i == s:
            print("Yes")
            exit()

print("No")
