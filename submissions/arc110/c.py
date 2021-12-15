n = int(input())
p = list(map(int,input().split()))

num = 1
ans = []

dic = {}


for i in range(n):
    dic[p[i]] = i
#print(dic)

while(num <= n):
    if num != dic[num]+1:
        for j in range(dic[num],num-1,-1):
            p[j],p[j-1] = p[j-1],p[j]
            ans.append(j)
            if j != dic[num] and p[j] != j+1:
                print(-1)
                exit()  
        num = dic[num]+1
    else:
        print(-1)
        exit()
    if len(ans) == n-1:
        break

if sorted(p) != p:
    print(-1)
    exit()


for i in ans:
    print(i)
