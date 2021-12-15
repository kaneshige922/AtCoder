p = int(input())

li = [1]
for i in range(2,11):
    li.append(li[-1]*i)

li.reverse()

ans = 0
i = 0
while(p!=0):
    ans += p//li[i]
    p -= p//li[i]*li[i]
    i += 1

print(ans)
