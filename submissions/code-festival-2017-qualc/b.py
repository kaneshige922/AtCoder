n = int(input())

a = list(map(int,input().split()))

total = 1
odd = 1

for i in a:
    total *= 3
    if i % 2 == 0:
        odd *= 2

    

print(total-odd)
