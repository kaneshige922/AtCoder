k =int(input())
s = input()
t = input()

num = [k]*9
sd = {}
td = {}
for i in range(1,10):
    sd[i] = 0
    td[i] = 0
for i in range(4):
    num[int(s[i])-1] -= 1
    num[int(t[i])-1] -= 1     
    sd[int(s[i])] += 1
    td[int(t[i])] += 1
     
sc = 0
tc = 0

for i in range(1,10):
    sc += i*(10**sd[i])
    tc += i*(10**td[i])

ko = 0

for i in range(1,10):
    for j in range(1,10):
        ws = sc + i*(10**(sd[i]+1)-10**sd[i])
        wt = tc + j*(10**(td[j]+1)-10**td[j])
        if ws > wt:
            if i == j and num[i-1] >= 2:
                ko += num[i-1]*(num[i-1]-1)
                
            elif i != j and num[i-1] >= 1 and num[j-1] >= 1:
                ko += num[i-1]*num[j-1]
                
nums = sum(num)

ans = ko/(nums*(nums-1))

print(ans)


