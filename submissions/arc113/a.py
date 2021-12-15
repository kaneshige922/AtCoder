k = int(input())

ans = 0
for i in range(1,k+1):
    for j in range(i,k+1):
        if i*j > k:
            break
        for l in range(j,k+1):
            if i*j*l > k:
                break
            else:
                if i == j and j == l:
                    ans += 1
                elif i == j or j == l:
                    ans += 3
                else:
                    ans += 6 

print(ans)
