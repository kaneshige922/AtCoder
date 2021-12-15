N,K = map(int,input().split())
C = list(map(int,input().split()))
count = 0
Clist = {}
for i in range(K):
    if str(C[i]) in Clist:
        Clist[str(C[i])] += 1
    else:
        Clist[str(C[i])] = 1
        count +=1
count_max = count
for i in range(N-K):
    if str(C[i]) in Clist:
        Clist[str(C[i])] -= 1
        if Clist[str(C[i])] == 0:
            Clist.pop(str(C[i]))
            count -= 1
    if str(C[i+K]) in Clist:
        Clist[str(C[i+K])] += 1
    else:
        Clist[str(C[i+K])] = 1
        count += 1
    if count_max < count:
        count_max = count
print(count_max)
