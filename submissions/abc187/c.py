### TLE
n = int(input())
s = []
ans = False
for i in range(n):
    s.append(input())
s = set(s)

for i in s:
    s1 = i
    if  "!" + i in s:
        ans = True
        break

if ans:
    print(s1)
else:
    print("satisfiable")
