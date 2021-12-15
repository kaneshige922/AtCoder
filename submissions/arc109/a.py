a,b,x,y =map(int,input().split())
ans = -1
if y <= 2*x:
    if a >b:
        ans = x + (abs(a-b)-1)*y
    else:
        ans = x + abs(a-b)*y
else:
    if a >b:
        ans = x + (abs(a-b)-1)*2*x
    else:
        ans = x + abs(a-b)*2*x
print(ans)
