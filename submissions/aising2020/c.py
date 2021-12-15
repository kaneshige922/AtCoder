n = int(input())

dic = {}

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            nn = x**2+y**2+z**2+x*y+y*z+z*x
            if nn in dic:
                dic[nn] += 1
            else:
                dic[nn] = 1

for i in range(1,n+1):
    if i in dic:
        print(dic[i])
    else:
        print(0)
