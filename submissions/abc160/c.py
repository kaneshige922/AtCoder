n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

d = [a[i+1]-a[i] for i in range(k-1)]
d.append(n-(a[k-1]-a[0]))

print(n-max(d))
