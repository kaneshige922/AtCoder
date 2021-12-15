n = int(input())

D = []
for i in range(n):
    c,d = map(int,input().split())
    if c == d:
        D.append(1)
    else:
        D.append(0)

for i in range(n-2):
    if D[i] + D[i+1] + D[i+2] == 3:
        print("Yes")
        exit()
print("No")
