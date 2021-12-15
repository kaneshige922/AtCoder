s = input()



if len(s) == 1:
    print("Yes")
    exit()

#case1

ans = False

for i in range(len(s)):
    if i % 3 == 0:
        if s[i] != "o":
            break
    else:
        if s[i] != "x":
            break
    if i == len(s)-1:
        ans = True


for i in range(len(s)):
    if i % 3 == 1:
        if s[i] != "o":
            break
    else:
        if s[i] != "x":
            break
    if i == len(s)-1:
        ans = True


for i in range(len(s)):
    if i % 3 == 2:
        if s[i] != "o":
            break
    else:
        if s[i] != "x":
            break
    if i == len(s)-1:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
