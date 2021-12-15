import numpy as np

n = int(input())

m = str(n)

if len(m) <= 2:
    print(0)
    exit()
ans = 0

for i in range(4**10):
    koho = []
    a = False
    b = False
    c = False
    k = str(np.base_repr(i,4))
    for j in k:
        if j == "1":
            koho.append("3")
            a =True
        elif j == "2":
            koho.append("5")
            b =True
        elif j == "3":
            koho.append("7")
            c =True
        else:
            a = b = c = False
            break
    if a and b and c:
        if int("".join(koho)) <= n:
            ans += 1
        else:
            print(ans)
            exit()

