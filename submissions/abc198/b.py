n = input()
l = len(n)

ans = False

for i in range(len(n)):
    m = n[::-1]
    if n == m:
        ans = True
        break
    n = str(0) + n
if ans:
    print("Yes")
else:
    print("No")
