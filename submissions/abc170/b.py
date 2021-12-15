x,y = map(int,input().split())

for i in range(x+1):
    if 4*i+2*(x-i) == y:
        print("Yes")
        exit()
print("No")
