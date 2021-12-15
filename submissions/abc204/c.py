import sys
sys.setrecursionlimit(100000)
from collections import deque 
n,m = map(int,input().split())
graph = [[] for i in range(n)]
total = 0
def goal(v):
    if temp[v]: return
    temp[v] = True
    for vv in graph[v]: 
        goal(vv)
for i in range(m):
    a,b= map(int,input().split())
    graph[a-1].append(b-1)
for i in range(n):
    temp = [False]*(n)
    goal(i)
    total += sum(temp)
print(total)
