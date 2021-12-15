n,q = map(int,input().split())
s = list(input())
lr = [list(map(int,input().split())) for i in range(q)]
acn = [0]*n

for i in range(1,n):
    if s[i-1] == "A" and s[i] == "C":
        acn[i] = acn[i-1] + 1
    else:
        acn[i] = acn[i-1]

for i in lr:
    print(acn[i[1]-1]-acn[i[0]-1])
