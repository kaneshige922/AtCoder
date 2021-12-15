n = int(input())
ans = ""
cnt = 1
t = False
mod = -1
memo = "0"
while n != 0:
    if n < cnt:
        if t:
            ad = mod
        else:
            ad = 1
            mod = 1
        #memo += str(ad)
        ans += str(ad)
        cnt = 1
        mod %= 7
        t = True
    else:
        ans += "7"
        n -= cnt
        cnt += 1
        if t:
            #memo += "0"
            mod *= 3
            mod %= 7

print(ans)
