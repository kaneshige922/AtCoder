n = int(input())
a = list(map(int,input().split()))

b = [0]*n
s = n-n//2-1
b[s] = a[0]
for i in range(1,n):
    if i % 2 != 0:
        b[s+i//2+1] = a[i]
    else:
        b[s-i//2] = a[i]

if n % 2 == 0:
    b.reverse()

b = [str(i) for i in b]

print(" ".join(b))

