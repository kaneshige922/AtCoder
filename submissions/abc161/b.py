n,m = map(int,input().split())
a =list(map(int,input().split()))
a.sort(reverse=True)

if 4*m*a[m-1] < sum(a):
    print("No")
else:
    print("Yes")
