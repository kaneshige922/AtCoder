import statistics

n = int(input())
a = list(map(int,input().split()))

a2 = [a[i]-(i+1) for i in range(n)]

b = statistics.median(a2)

ans = 0
for i in range(n):
    ans += abs(a2[i]-b)

print(int(ans))
