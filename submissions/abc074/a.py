
A,B,C,D,E,F = map(int,input().split())

ans = [A*100,0]

for a in range(F//(100*A)+1):
    for b in range((F-100*A*a)//(100*B)+1):
        if a == 0 and b == 0:
            continue
        f = 100*A*a + 100*B*b
        e = min(f//100*E,F-f)
        sato = 0
        for d in range(e//D+1):
            c = (e-D*d)//C
            sato = max(sato,C*c+D*d)
        if ans[1]*(sato+f)< sato*ans[0]:
            ans[0] = sato + f
            ans[1] = sato 

print(*ans)
