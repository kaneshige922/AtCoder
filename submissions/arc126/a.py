t = int(input())

for i in range(t):
    ans = 0
    z,y,x = map(int,input().split())
    y = y//2
    c = min(x,y)
    ans += c
    x -= c; y -= c
    c = min(y,z//2)
    ans += c
    y -= c; z -= 2*c
    c = min(x//2,z)
    ans += c
    x -= 2*c; z -= c
    c = min(x,z//3)
    ans += c
    x -= c; z -= 3*c
    ans += z//5
    print(ans)
