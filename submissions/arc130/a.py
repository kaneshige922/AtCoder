
n = int(input())
s = input()

ans = 0
cnt = 1
h = s[0]

for i in range(1,n):
    if s[i] == h:
        cnt += 1
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1
        h = s[i]


ans += cnt*(cnt-1)//2
print(ans)
