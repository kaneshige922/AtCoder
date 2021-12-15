
n = int(input())
a = list(map(int,input().split()))

dic = {}
dic[a[0]] = 1

ans = 0

for i in range(1,n):
    if a[i] in dic:
        ans += i - dic[a[i]]
        dic[a[i]] += 1
    else:
        ans += i
        dic[a[i]] = 1

print(ans)
