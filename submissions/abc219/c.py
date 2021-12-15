x = input()
dic1 = {}
dic2 = {}
for i in range(26):
    dic1[x[i]] = i
    dic2[i] = x[i]

n = int(input())

S = [list(input()) for i in range(n)]
nS = []
for i in S:
    s = []
    for j in range(len(i)):
        s.append(dic1[i[j]])
    nS.append(s)

nS.sort()

for i in nS:
    ans = ""
    for j in i:
        ans += dic2[j]
    print(ans)
