n,k = map(int,input().split())
d = set(map(int,input().split()))

for i in range(n,10**5):
    s = str(i)
    t = True
    for j in s:
        if int(j) in d:
            t = False
            break
    if t:
        print(i)
        exit()

