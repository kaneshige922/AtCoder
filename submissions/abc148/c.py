a,b = map(int,input().split())


for i in range(1,b+1):
    ans = a*i
    if ans % a == 0 and ans % b == 0:
        print(ans)
        exit()
