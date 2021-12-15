n,x = map(int,input().split())
s = list(input())
for i in s:
    if  i == "o":
        x += 1
    else:
        if x >= 1:
            x -= 1

print(x)
