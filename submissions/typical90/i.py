from collections import deque

q = int(input())

deck = deque()

for i in range(q):
    t,x = map(int,input().split())
    if(t==1):
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])
    
