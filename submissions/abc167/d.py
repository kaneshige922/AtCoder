n,k = map(int,input().split())
a = list(map(int,input().split()))

dic = {}
dic[1] = 0
root = [1]
now = 1

for i in range(1,k+1):
    now = a[now-1]
    if now not in dic:
        dic[now] = i
        k -= 1
        root.append(now)
    else:
        roop = i - dic[now]
        root.append(now)
        k -= 1
        k %= roop
        break

print(root[dic[now]+k])
