n,k,q = map(int,input().split())
a = [int(input()) for i in range(q)]

ok = [0]*n
score = [k]*n

for i in a:
    ok[i-1] += 1

for i in range(n):
    score[i] = k -(q-ok[i])

for i in range(n):
    if score[i] <= 0:
        print("No")
    else:
        print("Yes")
