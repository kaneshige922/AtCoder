
h,w = map(int,input().split())
C = [list(input()) for i in range(h)]

to = [[-1,0],[1,0],[0,-1],[0,1]]


for i in range(h):
    for j in range(w):
        if C[i][j] == ".":
            v = set()
            for dx,dy in to:
                if 0 <= i+dx < h and 0 <= j + dy < w:
                    if C[i+dx][j+dy] != ".":
                        v.add(int(C[i+dx][j+dy]))
            #print(i,j)
            #print(v)
            for k in range(1,6):
                if k not in v:
                    C[i][j] = str(k)
                    break
    
#print(C)

for i in C:
    print("".join(i))                

