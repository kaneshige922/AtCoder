
n,k,a = map(int,input().split())

for i in range(k-1):
    a += 1
    if a >= n+1:
        a = 1

print(a)
