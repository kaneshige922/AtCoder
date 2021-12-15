s = list(input())

count1=0; count2=0
s1 = []
s2 = []
for i in range(len(s)):
    if i % 2 == 0:
        s1.append("0")
        s2.append("1")
    else:
        s1.append("1")
        s2.append("0")

for i in range(len(s)):
    if s[i] == s1[i]:
        count2 +=1
    else:
        count1 +=1

print(min(count1,count2))
