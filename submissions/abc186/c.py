n = int(input())


ans = 0
t1 = t2 = True


for i in range(1,n+1):
    s1 = str(i)
    s2 = str(oct(i))
    for j in s1:
        if j == "7":
            t1 = False
    for j in s2:
        if j == "7":
            t2 = False
    if t1 and t2:
        ans += 1
    t1 = t2 = True

print(ans)
