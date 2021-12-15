import sys
import math
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

if abs(n-m) >= 2:
    print(0)
    exit()

if n == m:
    print(2*math.factorial(n)*math.factorial(m)%1000000007)
else:
    print(math.factorial(m)*math.factorial(n)%1000000007)

     
