n = int(input())
n = list(str(n))
nl = len(n)
k= 0
nlis = [[],[],[]]
for i in n:
    k += int(i)
    nlis[int(i)%3].append(int(i))
ama = k % 3
if ama == 0:
    print(0)
elif len(nlis[ama]) >= 1 and nl >= 2:
    print(1)
elif ama == 1 and len(nlis[2]) >= 2 and nl >=3:
    print(2)
elif ama == 2 and len(nlis[1]) >= 2 and nl >=3:
    print(2)
else:
    print(-1)
