
n = int(input())


ans = 0

for a in range(1,n+1):
    if a*a > n:
        break
    NC = n//a
    for b in range(a,n+1):
        if b*b > NC:
            break
        #print(a,b,max(min(n//(a*c)-a+1,c-a+1),0))
        ans += max(n//(a*b)-b+1,0)



print(ans)
