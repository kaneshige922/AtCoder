import math

x = int(input())
if x == 2:
    print(2)
    exit()
for i in range(10**5):
    for j in range(2,math.ceil(math.sqrt(x+i)+1)):
        if (x+i) % j == 0:
            break
        if j == math.ceil(math.sqrt(x+i)):
            print(x+i)
            exit()
