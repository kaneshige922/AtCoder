x = int(input())

ans = 2*(x // 11) 

if x % 11 >= 7:
    ans += 2
elif x % 11 >= 1:
    ans += 1

print(ans)

