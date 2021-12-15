N = int(input())
S = input()
count = 1 
for i in range(N):
    if int(S[i]) == 1:
        if count % 2 == 0:
            print("Aoki")
        else:
            print("Takahashi")
        break
    count += 1
