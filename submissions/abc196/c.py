n = int(input())
s = str(n)
l = len(s)
if l % 2 == 1:
    print(int(10**((l-1)/2)-1))
else:
    z = 0
    for i in range(l//2):
        if i == 0:
            z += (int(s[i])-1)*(10**(l/2-1-i))
        else:
            z += int(s[i])*(10**(l/2-1-i))
    if int(s[:(l//2)]) <= int(s[(l//2):]):
        z += 1
    print(int(10**((l-2)/2)-1+z))
