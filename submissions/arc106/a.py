n = int(input())

for i in range(1,1000):
    if 5**i > n:
        break
    for j in range(1,1000):
        if 5**i + 3**j == n:
            print(j,i)
            exit()
        elif 5**i + 3**j > n:
            break

print("-1")
