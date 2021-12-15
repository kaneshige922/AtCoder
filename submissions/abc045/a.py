s = list(input())
#s = [int(i) for i in s]

slen = len(s)-1

ans = 0

for i in range(2**slen):
    ch = s[0]
    for j in range(slen):
        if i>>j & 1:
            ans += int(ch)
            ch = s[j+1]
        else:
            ch += s[j+1]
        #print(ch)
    ans += int(ch)


print(ans)
