import heapq

x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)


A = []
B = []
acnt = 0
bcnt = 0

for i in range(min(x,a)):
    heapq.heappush(A,p[i])
    acnt += 1
for i in range(min(y,b)):
    heapq.heappush(B,q[i])
    bcnt += 1

for i in range(c):
    if acnt == x and bcnt == y:
        if A[0] >= B[0]:
            if B[0] <= r[i]:
                heapq.heapreplace(B,r[i])
        else:
            if A[0] <= r[i]:
                heapq.heapreplace(A,r[i])
    elif acnt != x:
        heapq.heappush(A,r[i])
        acnt += 1
    else:
        heapq.heappush(B,r[i])
        bcnt += 1


ans = sum(A) + sum(B)

print(ans)
