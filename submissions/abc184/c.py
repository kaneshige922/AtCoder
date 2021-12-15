r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

if r1 == r2 and c1 == c2:
    print(0)
elif abs(r1-r2) == abs(c1-c2) or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
elif abs(abs(r1+c1)-abs(r2+c2)) % 2 == 0:
    print(2)
elif abs(r1-r2) + abs(c1-c2) <= 6:
    print(2)
elif (r2-r1+c1-c2)**2/2 <= 9 or (r1-r2+c1-c2)**2/2 <= 9:
    print(2)
else:
    print(3)
