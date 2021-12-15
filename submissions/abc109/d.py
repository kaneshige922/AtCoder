h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]

cnt = 0
sousa = []
for i in range(h):
    for j in range(w):
        if i == h-1 and j == w-1:
            print(cnt)
            for k in sousa:
                print(*k)
            exit()
        elif j == w-1:
            if a[i][j] % 2 != 0:
                a[i+1][j] += 1
                cnt += 1
                sousa.append([i+1,j+1,i+2,j+1])
        else:
            if a[i][j] % 2 != 0:
                a[i][j+1] += 1
                cnt += 1
                sousa.append([i+1,j+1,i+1,j+2])

        
