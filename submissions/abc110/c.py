s = list(input())
t = list(input())

dicS = {}
dicT = {}
for i in range(len(s)):
    if (s[i] not in dicS) and (t[i] not in dicT):
        dicS[s[i]] = t[i]
        dicT[t[i]] = s[i]
    elif s[i] in dicS:
        if dicS[s[i]] != t[i]:
            print("No")
            exit()
    elif t[i] in dicT:
        if dicT[t[i]] != s[i]:
            print("No")
            exit()
print("Yes")
