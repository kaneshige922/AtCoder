N = int(input())
A = list(map(int,input().split())) 
count = 0
for i in range(100):
    t = 0
    for j in range(N):
        if A[j] % 2 == 0:
            A[j] = A[j]/2
        else:
            t +=1
            break
    if t == 0:
        count += 1
    else:
        break
print(count)
