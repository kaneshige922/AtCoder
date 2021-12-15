n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ba = sum(a)
for i in range(n):
    hiku =  min(a[i],b[i])
    a[i] -= hiku
    b[i] -= hiku
    a[i+1] -= min(a[i+1],b[i])

aa = sum(a)

print(ba-aa)
