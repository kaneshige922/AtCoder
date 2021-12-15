n = int(input())
m = []
for i in range(n):
    m.append(list(input().split()))
    m[i][1] = int(m[i][1])
m.sort(reverse=True,key = lambda x: x[1])
print(m[1][0])
