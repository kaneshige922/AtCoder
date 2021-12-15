import math

n = input()
t = True

for i in range(len(n)):
    if n[i] == ".":
        print(n[:i])
        t = False
        break
if t:
    print(n)
