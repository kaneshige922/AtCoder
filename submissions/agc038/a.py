h,w,a,b = map(int,input().split())



for i in range(1,h+1):
    ans = ""
    if i <= b:
        for j in range(1,w+1):
            if j <= a:
                ans += "1"
            else:
                ans += "0"
    else:
        for j in range(1,w+1):
            if j <= a:
                ans += "0"
            else:
                ans += "1"
    print(ans)

