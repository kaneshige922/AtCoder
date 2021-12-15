from collections import deque

n,m = map(int,input().split())
a = deque(sorted(list(map(int,input().split())),reverse=True))
bc = [list(map(int,input().split())) for i in range(m)]

bc.sort(key=lambda x:x[1],reverse=True)

ans = deque()

for i in bc:
    b = i[0]
    c = i[1]
    while a[0] >= i[1]:
            h = a.popleft()
            ans.append(h)
            if not(a):
                print(sum(ans))
                exit()
    while b > 0 and a[-1] < i[1]:
        a.pop()
        ans.append(i[1])
        b -= 1
        if not(a):
            print(sum(ans))
            exit()

ans = ans + a
print(sum(ans))

        
        

