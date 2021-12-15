N,Y = map(int,input().split())
count = 0
for i in range(min(Y//10000+1,N+1)):
    Y1 = Y - 10000*i
    for j in range(min(Y1//5000+1,N+1-i)):
        Y2 = Y1 - 5000*j
        if Y2/1000 == N - i - j:
            k = int(Y2/1000)
            print(i,j,k)
            count +=1
    if count == 1:
        break
if count == 0:
    print(-1,-1,-1)
