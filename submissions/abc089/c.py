n = int(input())
s = [input() for i in range(n)]

names = [0]*5

for i in s:
    if i[0] == "M":
        names[0] += 1
    elif i[0] == "A":
        names[1] += 1
    elif i[0] == "R":
        names[2] += 1
    elif i[0] == "C":
        names[3] += 1
    elif i[0] == "H":
        names[4] += 1

ans = 0

for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans += names[i]*names[j]*names[k]

print(ans)
