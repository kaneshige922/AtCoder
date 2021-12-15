s = list(input())
k = int(input())

ans = ""

for i in s:
    if (123-ord(i)) <= k and i != "a":
        ans += "a"
        k -= 123-ord(i)
    else:
        ans += i
if(k > 0):
    ans = ans[:-1] + chr(ord(ans[-1])+k%26)

print(ans)
