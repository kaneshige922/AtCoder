import math

n = int(input())

keta = -1
if n >= 0:
    t = 1
    while n > 2 + 4*(4**(t-1)-1)//3-1:
        t += 1
    keta = 2*t -1
else:
    t = 1
    while -n > 2*(4**t-1)//3:
        t += 1
    keta = 2*t


ans = []
""""
if (keta-1) % 2 == 0:
    n -= 2**(keta-1)
else:
    n += 2**(keta-1)
"""

for i in range(keta):
    k = keta-i-1
    if k == 0:
        if n == 1:
            ans.append("1")
        else:
            ans.append("0")
        break
    if k % 2 == 0:
        if  n > 2 + 4*(4**((k-2)//2)-1)//3-1 :
            #n >= 2 + 4*(4**(k//2)-1)//3-1 or
            ans.append("1")
            n -= 2**k
        else:
            ans.append("0")
    else:
        if n < -2*(4**((k-1)//2)-1)//3:
            #n >= -2*(4**((k+1)//2)-1)//3 or 
            ans.append("1")
            n += 2**k
        else:
            ans.append("0")

print("".join(ans))
