s = input()[::-1]
s = "0" + s
num = []
dic = {}
n,d = 0,1
for i in s:
    n += int(i)*d
    n %= 2019
    d *= 10
    d %= 2019
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

ans = 0
for i in dic:
    if dic[i] >= 2:
        ans += dic[i]*(dic[i]-1)//2

print(ans)
