n = int(input())
h = list(map(int,input().split()))
h.reverse()
for i in range(1,n):
    if h[i-1] == h[i]-1:
        h[i] -= 1
    elif h[i] - h[i-1] > 1:
        print("No")
        exit()

print("Yes")

