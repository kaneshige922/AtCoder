n,m = map(int,input().split())

if n >= m//2:
    print(m//2)
    exit()
else:
    ans =(m - 2*n) // 4 + n 
    print(ans)
