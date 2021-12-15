n = int(input())
s = input()

black = [0]*(n+1)
white = [0]*(n+1)

for i in range(n):
    if s[i] == "#":
        black[i+1] = black[i] + 1
        white[i+1] = white[i]
    else:
        black[i+1] = black[i] 
        white[i+1] = white[i] + 1


ans = float("inf")
for i in range(n+1):
    ans = min(black[i]+white[n]-white[i],ans)

print(ans)
