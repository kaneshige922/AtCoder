x = input()

if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    print("Weak")
    exit()
for i in range(3):
    if int(x[i]) != 9:
        if int(x[i])+1 != int(x[i+1]):
            print("Strong")
            exit()
    elif int(x[i+1]) != 0:
        print("Strong")
        exit()
print("Weak")

