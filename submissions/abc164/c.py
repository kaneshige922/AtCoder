n = int(input())
s = [input() for i in range(n)]

get = set()
ans = 0

for i in s:
    if not(i in get):
        ans += 1
        get.add(i)

print(ans)
