n = int(input())
a = list(map(int,input().split()))
b = [0]*n
t = True

for i in range(n-1):
    if t:
        if a[i] > a[i+1]:
            b[i] = 1
            t = not(t)
        else:
            b[i] = 0
    else:
        if a[i] < a[i+1]:
            b[i] = 1
            t = not(t)
        else:
            b[i] = 0

if sum(b)%2 != 0:
    b[n-1] = 1

print(*b)
        

    
