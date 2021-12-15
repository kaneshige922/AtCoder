n = int(input())
a = [int(input()) for i in range(n)]

pa = set()

for i in a:
    if i in pa:
        pa.remove(i)
    else:
        pa.add(i)

list(pa)

print(len(pa))
