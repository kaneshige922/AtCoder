x,y,z = map(int,input().split())

memo = [[[None for k in range(101)]for j in range(101)]for i in range(101)]



def dpp(a,b,c):
    if memo[a][b][c] == None:
        if a == 100 or b == 100 or c ==100:
            d = 0
        else:
            d = a/(a+b+c)*(dpp(a+1,b,c)+1) + b/(a+b+c)*(dpp(a,b+1,c)+1) + c/(a+b+c)*(dpp(a,b,c+1)+1)
        memo[a][b][c] = d
    return memo[a][b][c]

print(dpp(x,y,z))
