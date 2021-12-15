from collections import deque

k = int(input())
q = deque([1,2,3,4,5,6,7,8,9])

a = 0

for i in range(k):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10*a+a%10-1)
    q.append(10*a+a%10)
    if a % 10 != 9:
        q.append(10*a+a%10+1)


print(a)
