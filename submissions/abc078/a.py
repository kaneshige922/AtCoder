n,m = map(int,input().split())

p = 1/2**m
q = 1 - p

ans = (1900*m+100*(n-m))*p/(1-q)**2

print(int(ans))
