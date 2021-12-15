
a,b = input().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()


for i in range(min(len(a),len(b))):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard")
        exit()

print("Easy")
