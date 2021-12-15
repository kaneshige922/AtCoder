def yakusu(n):
    import math
    ylist = []
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i == n//i:
                ylist.append(i)
            else:
                ylist.append(i)
                ylist.append(n//i)
    ylist.sort()
    return ylist


n = int(input())
y = yakusu(n)
for i in y:
    for j in range(n):
        if j**5 - (j-i)**5 == n:
            print(j,j-i)
            exit() 
        elif j**5-(j-i)**5>n and j-i>=0:
            break 
