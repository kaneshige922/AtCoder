a,b,c = map(int,input().split())

ans = (3*max(a,b,c)-a-b-c)

if ans % 2 == 0:
    print(ans//2)
else:
    print((ans+1)//2 + 1)
