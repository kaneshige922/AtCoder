n = int(input())
a = list(map(int,input().split()))
ori = a
for i in range(n-1):
    a1 = []
    for j in range(2**(n-(i+1))):
        a1.append(max(a[2*j],a[2*j+1]))
    a = a1
for i in range(2**n):
    if ori[i] == min(a):
        print(i+1)
