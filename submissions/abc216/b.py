n = int(input())
st = [tuple(input().split()) for i in range(n)]

v = set()

for i in st:
    if i in v:
        print("Yes")
        exit()
    else:
        v.add(i)

print("No")
