import itertools
import math

n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
num = [i for i in range(n)]

kumi = itertools.permutations(num)

def kai(n):
    if n != 0:
        return n*kai(n-1)
    else:
        return 1

ans = 0

for k in kumi:
    kyori = 0
    for j in range(n-1):
        kyori += math.sqrt((xy[k[j+1]][0]-xy[k[j]][0])**2 + (xy[k[j+1]][1]-xy[k[j]][1])**2)
    ans += kyori
ans = ans/kai(n)

print(ans)
