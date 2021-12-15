n = list(input())
n = [int(i) for i in n]
s = sum(n)

if s % 9 == 0:
    print("Yes")
else:
    print("No")
