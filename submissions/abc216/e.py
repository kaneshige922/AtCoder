
n,k = map(int,input().split())
a = list(map(int,input().split()))


if sum(a) <= k:
    ans = 0
    for i in a:
        ans += i*(i+1)//2
    print(ans)
    exit()


#“ñ•ª’Tõ
def ok(line):
    cnt = 0
    for i in a:
        if i >= line:
            cnt +=  i-line
    return cnt <= k

left = 0
right = 2*10**9

while right - left > 1:
    mid = (right+left)//2
    if ok(mid):
        right = mid
    else:
        left = mid

ans = 0

for i in a:
    if i >= right:
        k -= i-right
        ans += (i-right)*(i+right+1)//2

ans += k*right

print(ans)
