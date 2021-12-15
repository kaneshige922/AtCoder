
n = int(input())

ans = [0]*(n+1)
ans[1] = 1

for i in range(2,n+1):
    ins = 1
    for j in range(1,i+1):
        if j*j > i:
            break
        if i % j == 0:
            ins = max(ins,ans[j],ans[i//j])
    ans[i] = ins+1

print(*ans[1:])
