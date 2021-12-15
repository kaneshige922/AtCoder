from itertools import permutations

s1 = input()
s2 = input()
s3 = input()

v = set()
if s1 == s3 or s2 == s3:
    print("UNSOLVABLE")
    exit()


for i in s1:
    v.add(i)
for i in s2:
    v.add(i)
for i in s3:
    v.add(i)

if len(v) > 10:
    print("UNSOLVABLE")
    exit()

v = sorted(list(v))
dic = {}
for i in v:
    dic[i] = 0


num = [i for i in range(10)]
n = len(v)
numl = list(permutations(num,n))

a = len(s1)
b = len(s2)
c = len(s3)


for i in permutations(num,n):
    x = 0
    y = 0
    z = 0
    for j in range(n):
        dic[v[j]] = i[j]
    if dic[s1[0]] == 0 or dic[s2[0]] == 0 or dic[s3[0]] == 0:
        continue
    for j in range(a):
        x += dic[s1[j]]*(10**(a-1-j))
    for j in range(b):
        y += dic[s2[j]]*(10**(b-1-j))
    for j in range(c):
        z += dic[s3[j]]*(10**(c-1-j))
    if x + y == z:
            print(x)
            print(y)
            print(z)
            exit()

print("UNSOLVABLE")

