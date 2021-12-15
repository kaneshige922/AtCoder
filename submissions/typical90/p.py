k = int(input())

if k%9!=0:
    print(0)
    exit()

memo = [-1 for i in range(k+1)]
memo[0] = 1
mod = 1000000007

def saiki(x):
    if x < 0:
        return 0
    elif memo[x] != -1:
        return memo[x]
    else:
        k = 0
        for i in range(1,10):
            k += saiki(x-i)
        return k%mod
    
for i in range(1,k+1):
    memo[i] = saiki(i)

print(memo[k])
