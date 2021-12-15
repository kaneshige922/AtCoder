n = int(input())

ans = str()

while n != 0:
    if n % 2 == 0:
        n //= 2
        ans += "B"
    else:
        n -= 1
        ans += "A"


ans = reversed(list(ans))


print("".join(ans))
