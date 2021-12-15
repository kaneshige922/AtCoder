n = int(input())
a = list(map(int,input().split()))

s = set()
all = 0
for i in a:
    if i < 400:
        s.add(1)
    elif i < 800:
        s.add(2)
    elif i < 1200:
        s.add(3)
    elif i < 1600:
        s.add(4)
    elif i < 2000:
        s.add(5)
    elif i < 2400:
        s.add(6)
    elif i < 2800:
        s.add(7)
    elif i < 3200:
        s.add(8)
    else:
        all += 1

s = list(s)

print(max(len(s),1),len(s)+all)
