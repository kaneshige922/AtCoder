n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

upper = sum(b) -sum(a)

def myceil(a,b):
    return a//b + (a%b!=0)


cnta = 0
cntb = 0


for i in range(n):
    if a[i] >= b[i]:
        cntb += a[i]-b[i]
    else:
        cnta += myceil(b[i]-a[i],2)
        cntb += (b[i]-a[i])%2 

#print(cnta,cntb)
if cnta > cntb:
    cnta += cnta-cntb


if max(cnta,cntb) == upper:
    print("Yes")
else:
    print("No")
