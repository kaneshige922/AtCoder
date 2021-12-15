s = list(input())
t = list(input())

if s==t:
    print("Yes")
    exit()


for i in range(len(s)-1):
    s2 = s[:i] + [s[i+1]] +[s[i]] + s[i+2:]
    if s2 == t:
        print("Yes")
        exit()

print("No")
