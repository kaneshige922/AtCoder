n,m = map(int,input().split())
bro = set()
for i in range(m):
    bro.add(int(input()))

b = [0]*n

if 1 in bro:        
    b[0] = 0
else:
    b[0] = 1
if n == 1:
    print(1)
    exit()
if 2 in bro:
    b[1] = 0
else:
    b[1] = b[0] + 1        
if n == 2:
    print(b[1])
    exit()

for i in range(3,n+1):
    if i in bro:
        b[i-1] = 0
    else:
        b[i-1] = b[i-2] + b[i-3]
    

print(b[n-1]%1000000007)
