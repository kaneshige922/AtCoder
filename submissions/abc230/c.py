N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())


#step1 
low = max(1-A,1-B)
high = max(N-A,N-B)
low2 = max(1-A,B-N)
high2 = min(N-A,B-1)



g = [["." for i in range(S-R+1)] for j in range(Q-P+1)]



for i in range(Q-P+1):
    for j in range(S-R+1):
        if P+i-A == R+j-B:
            if P+i-A >= low and P+i-A <= high:
                g[i][j] = "#"
        elif P+i-A == B-R-j:
            if P+i-A >= low2 and P+i-A <= high2:
                g[i][j] = "#"


for i in g:
    print("".join(i))
