n,k = map(int,input().split())


if n == 0:
    print(0)
    exit()

for i in range(k):
    s = str(n)
    n = 0
    for j in range(len(s)):
        n += int(s[-(j+1)])*(8**j)
    nn = ""
    cnt = 1
    while(n!=0):
        a = n%(9**cnt)//(9**(cnt-1))
        n -= a*(9**(cnt-1))
        if a==8:
            nn = "5" + nn
        else:
            nn = str(a) + nn
        cnt += 1
    n = int(nn)



print(n)

