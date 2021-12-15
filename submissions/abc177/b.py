s = input()
t = input()

ls = len(s)
lt = len(t)
ans = lt

for i in range(ls-lt+1):
    count = 0
    for j in range(lt):
        if s[i+j] != t[j]:
            count += 1
    ans = min(count,ans)

print(ans)

