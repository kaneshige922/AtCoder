
n = int(input())
L = set()
for i in range(n):
    l = tuple(list(input().split()))
    L.add(l)

print(len(list(L)))
