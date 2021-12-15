import copy

s = list(input())
s = [int(i) for i in s]
a = [0]*10

if len(s) == 1:
    if s[0] % 8 == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
elif len(s) == 2:
    if (10*s[0]+s[1]) % 8 == 0 or (10*s[1]+s[0])%8==0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()



for i in s:
    a[i] += 1

for j in range(125):
    z = j*8
    b = copy.deepcopy(a)
    z = str(z).zfill(3)
    if b[int(z[0])]>=1:
        b[int(z[0])] -= 1
        if b[int(z[1])]>=1:
            b[int(z[1])] -= 1
            if b[int(z[2])]>=1:
                print("Yes")
                exit()

print("No")


