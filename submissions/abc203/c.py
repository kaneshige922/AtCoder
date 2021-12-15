n,k = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]
ab.sort()


h = 0
for i in ab:
    if i[0]-h > k:
        print(h+k)
        exit()
    else:
        k -= i[0]-h
        h = i[0]
        k += i[1]

print(h+k)
