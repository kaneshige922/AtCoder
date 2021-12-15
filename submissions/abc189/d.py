n = int(input())
s = [input() for i in range(n)]
if s[0] == "AND":
    p = 1
    q = 3 
else:
    p = 3
    q = 1
for i in range(1,n):
    if s[i] == "AND":
        q = 2**(i+2)-p
    else:
        p = 2*p + q
        q = 2**(i+2)-p

print(p)
