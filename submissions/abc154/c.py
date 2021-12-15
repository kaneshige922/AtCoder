n = int(input())
a = list(map(int,input().split()))

s = set()


for i in a:
    if i in s:
        print("NO")
        exit()
    else:
        s.add(i)

print("YES")
