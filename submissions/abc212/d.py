import heapq

q = int(input())

box = []

cnt = 0
for i in range(q):
    x = list(map(int,input().split()))
    if x[0] == 1:
        heapq.heappush(box,x[1]-cnt)
    elif x[0] == 2:
        cnt += x[1]
    else:
        print(heapq.heappop(box)+cnt)
