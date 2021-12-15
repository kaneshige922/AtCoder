x = input()

if int(x[-1]) < 3:
    print(x[:-2]+"-")
elif int(x[-1]) < 7:
    print(x[:-2])
else:
    print(x[:-2]+"+")
