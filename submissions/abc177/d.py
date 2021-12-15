from collections import deque

n,m = map(int,input().split())
ab = [set() for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    ab[a-1].add(b-1)
    ab[b-1].add(a-1)

vi1 = set()
qu = deque()
for i in range(n):
    if i not in vi1:
        vi1.add(i)
        qu.append(i)
        while qu:
            h = qu.popleft()
            if h != i:
                ab[i].add(h)
            for j in ab[h]:
                if j not in vi1:
                    qu.append(j)
                    vi1.add(j)

ans = 0
for i in range(n):
    ans = max(ans,len(ab[i]))

print(ans+1)
