n = int(input())
a = list(map(int,input().split()))
s = [i for i in range(1,n+1)]
a.sort()
if a == s:
    print("Yes")
else:
    print("No")
