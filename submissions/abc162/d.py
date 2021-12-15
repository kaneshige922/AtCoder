n = int(input())
s = input()
rgb = [set() for i in range(3)]
for i in range(n):
    if s[i] == "R":
        rgb[0].add(i)
    elif s[i] == "G":
        rgb[1].add(i)
    else:
        rgb[2].add(i)


ans = 1
for i in range(3):
    ans *= len(rgb[i])
    
for i in rgb[0]:
    for j in rgb[1]:
        if 2*i-j in rgb[2]:
            ans -= 1
        if 2*j-i in rgb[2]:
            ans -= 1
        if (i+j) % 2 == 0 and (i+j)//2 in rgb[2]:
            ans -= 1

print(ans)

        

    
