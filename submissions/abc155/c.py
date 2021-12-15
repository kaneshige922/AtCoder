n = int(input())
ans = dict()
alis = []
count = 0
for i in range(n):
    a = input()
    if a in ans:
        alis[ans[a]][1] += 1
    else:  
        ans[a] = count
        alis.append([a,1])
        count +=1
alis.sort(reverse = True,key = lambda x : x[1])

kotae = []
amax = 0
for i in range(len(alis)):
    if amax <= alis[i][1]:
        kotae.append(alis[i][0])
        amax = alis[i][1]
    else:
        break
kotae.sort()
for i in kotae:
    print(i)
