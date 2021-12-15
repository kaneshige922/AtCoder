import math

n = int(input())
a = list(map(int,input().split()))

dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 0
dic2 = {}
dic3 = {}
for i in dic:
    if dic[i] >= 2:
        dic2[i] = math.factorial(dic[i])/(2*math.factorial(dic[i]-2))
        ans += dic2[i]
    if dic[i] >= 3:
        dic3[i] = math.factorial(dic[i]-1)/(2*math.factorial(dic[i]-3))
for i in a:
    if dic[i] == 2:
        print(int(ans-dic2[i]))
    elif dic[i] == 1:
        print(int(ans))
    else:
        print(int(ans-dic2[i]+dic3[i]))
