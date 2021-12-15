from collections import deque
import heapq

q = int(input())
qu = []
for i in range(q):
    qu.append(list(map(int,input().split())))

qu1 = deque()
qu2 = []
#print("==============================")
for i in qu:
    if i[0] == 1:
        qu1.append(i[1])
    elif i[0] == 2:
        if len(qu2) == 0:
            print(qu1.popleft())
        else:
            print(heapq.heappop(qu2))
    else:
        while(qu1):
            heapq.heappush(qu2,qu1.popleft())


 
