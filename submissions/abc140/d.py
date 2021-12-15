
n,k = map(int,input().split())
s = list(input())


flag = s[0]
Lcnt = 0
Rcnt = 0
ans = 0

for i in range(1,n):
    if s[i] == flag:
        ans += 1
    else:
        if flag == "R":
            Rcnt += 1
            flag = "L"
        else:
            Lcnt += 1
            flag = "R"
if flag == "R":
    Rcnt += 1
    flag = "L"
else:
    Lcnt += 1
    flag = "R"


X = min(Lcnt,Rcnt)

print(min(ans+2*min(k,X),n-1))
