from typing import List


n = int(input())
l = list(map(int,input().split()))


ans = 0


for i in range(n-2):
    for j in range(i+1,n-1):
            for k in range(j+1,n):
                    if not(l[i] == l[j] or l[j]==l[k] or l[k]==l[i]) and 2*max(l[i],l[j],l[k]) < sum([l[i],l[j],l[k]]):
                        ans += 1


print(ans)
