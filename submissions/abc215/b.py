n = int(input())

for i in range(61):
    if 2**i > n:
        print(i-1)
        exit()
