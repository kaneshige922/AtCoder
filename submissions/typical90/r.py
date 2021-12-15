n,q = map(int,input().split())
a = list(map(int,input().split()))

queri = [list(map(int,input().split())) for i in range(q)]

cnt = 0

for i in queri:
    if i[0] == 1:
        sa = a[(i[1]-1-cnt)%n]
        a[(i[1]-1-cnt)%n] = a[(i[2]-1-cnt)%n]
        a[(i[2]-1-cnt)%n] = sa
    elif i[0] == 2:
        cnt += 1
    else:
        print(a[(i[1]-1-cnt)%n])

