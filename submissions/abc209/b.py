N,X = map(int,input().split())
A = list(map(int,input().split()))
sums = 0
for i in range(N):
    if i % 2 == 0 :
        sums += A[i]
    else:
        sums += A[i]-1
if sums > X:
    print("No")
else:
    print("Yes")
