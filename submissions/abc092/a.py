n = int(input())
a = list(map(int,input().split()))
a = [0] + a + [0]
cost = [0]*(n+1)
for i in range(1,n+2):
    cost[i-1] = a[i] - a[i-1]

bc = 0
for i in cost:
    bc += abs(i)

for i in range(1,n+1):
    print(bc-((abs(cost[i-1])+abs(cost[i]))-abs(cost[i-1]+cost[i])))
