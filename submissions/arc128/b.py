t = int(input())
case = [list(map(int,input().split())) for i in range(t)]

for i in case:
    R = i[0]
    G = i[1]
    B = i[2]
    ans = -1
    if sum(i) == 0:
        print(-1)
        continue
    elif sum(i) == 1:
        print(0)
        continue
    else:
        if abs(G-B)%3 == 0:
            R1 = R + 2*min(G,B)
            G1 = G - min(G,B)
            B1 = B - min(G,B)
            cnt = min(G,B)
            #if R1 >= abs(G1-B1)//3:
            cnt += abs(G1-B1)
            if ans == -1:
                ans = cnt
            else:
                ans = min(ans,cnt)
        if abs(R-G)%3 == 0:
            R1 = R - min(R,G)
            G1 = G - min(R,G)
            B1 = B + 2*min(R,G)
            cnt = min(R,G)
            #if B1 >= abs(R1-G1)//3:
            cnt += abs(R1-G1)
            if ans == -1:
                ans = cnt
            else:
                ans = min(ans,cnt)
        if abs(B-R)%3 == 0:
            R1 = R - min(R,B)
            G1 = G + 2*min(R,B)
            B1 = B - min(R,B)
            cnt = min(R,B)
            #if G1 >= abs(R1-B1)//3:
            cnt += abs(R1-B1)
            if ans == -1:
                ans = cnt
            else:
                ans = min(ans,cnt)
        print(ans)



