t = int(input())
n = [int(input()) for i in range(t)]

def oe(a):
    if a == 2:
        print("Same")
    elif a % 2 == 0:
        if a % 4 == 0:
            print("Even")
        else:
            print("Same")
    else:
        print("Odd")

for i in n:
    oe(i)
