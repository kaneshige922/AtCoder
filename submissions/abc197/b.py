h,w,x,y = map(int,input().split())
s = []
for i in range(h):
    s1 = input()
    s.append(list(s1))
if s[x-1][y-1] == "#":
    print(0)
else:
    count = 1
    for i in range(1,x):
        if s[x-1-i][y-1] == ".":
            count +=1
        else:
            break
    for i in range(1,h-x+1):
        if s[x-1+i][y-1] == ".":
            count +=1
        else:
            break
    for i in range(1,y):
        if s[x-1][y-1-i] == ".":
            count +=1
        else:
            break
    for i in range(1,w-y+1):
        if s[x-1][y-1+i] == ".":
            count +=1
        else:
            break
    print(count)
