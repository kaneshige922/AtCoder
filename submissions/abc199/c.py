n = int(input())
s = list(input())
q = int(input())
tab = [list(map(int,input().split())) for i in range(q)]

cnt = 0
for i in tab:
    if i[0] == 1:
        if cnt % 2 == 0:
            k = s[i[1]-1]
            s[i[1]-1] = s[i[2]-1]
            s[i[2]-1] = k
        else:
            if i[1]-1 <= n-1:
                if i[2]-1 <= n-1:
                    k = s[n+i[1]-1]
                    s[n+i[1]-1] = s[n+i[2]-1]
                    s[n+i[2]-1] = k
                else:
                    k = s[n+i[1]-1]
                    s[n+i[1]-1] = s[i[2]-1-n]
                    s[i[2]-1-n] = k
            else:
                if i[2]-1 <= n-1:
                    k = s[i[1]-1-n]
                    s[i[1]-1-n] = s[n+i[2]-1]
                    s[n+i[2]-1] = k
                else:
                    k = s[i[1]-1-n]
                    s[i[1]-1-n] = s[i[2]-1-n]
                    s[i[2]-1-n] = k
    else:
        cnt +=1
if cnt % 2 == 1:
    bs = s[:n]
    sb = s[n:]
    s = sb + bs

print("".join(s))

    
