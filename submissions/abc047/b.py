n,t = map(int,input().split())
a = list(map(int,input().split()))


left = a[0]
right = a[0]

benefit = -1
cnt = 0


for i in a[1:]:
    if i < left:
        bf = right -left
        if bf > 0:
            if bf == benefit:
                cnt += 1
            elif bf > benefit:
                benefit = bf
                cnt = 1
        left = i
        right = i
    elif right < i:
        right = i

bf = right - left
if bf > 0:
    if bf == benefit:
        cnt += 1
    elif bf > benefit:
        benefit = bf
        cnt = 1


print(cnt)


