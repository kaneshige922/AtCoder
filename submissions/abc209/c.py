N = int(input())
C = list(map(int,input().split()))
count = 1
C.sort()
for i in range (N):
    count = count*(C[i]-i)
    if count == 0:
        break
    elif count >= 1000000007:
        count = count % 1000000007
print(count%(10**9+7))
