n = int(input())
a = list(map(int,input().split()))

s1 = set()
s2 = []

for i in a:
    if not(i in s1):
        s1.add(i)
    else:
        s2.append(i)
        s1.remove(i)

s2.sort(reverse = True)
if len(s2) >= 2:
    print(s2[0]*s2[1])
else:
    print(0)
