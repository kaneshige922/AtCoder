a,b,c = map(int,input().split())

ans = 0

if b-a < c-b:
    if (c-2*b+a) % 2 == 0:
            ans = (c-2*b+a)//2
    else:
        ans = (c-2*b+a)//2 + 2
elif b-a > c-b:
    ans = 2*b-a-c

print(ans)
