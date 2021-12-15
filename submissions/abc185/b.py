n,m,t = map(int,input().split())
ab = [0]


z = n
ans = True

for i in range(m):
    a,b =  map(int,input().split())
    ab.append(a)
    ab.append(b)
ab.append(t)

for i in range(2*m+1):
    if i % 2  == 0:
        z -= ab[i+1] - ab[i]
        if z <= 0:
            ans = False
            break
    else:
        z += ab[i+1] - ab[i]
        z = min(n,z)
if ans:
    print("Yes")
else:
    print("No")
