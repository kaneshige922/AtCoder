a = list(input())

dic = {}

for i in range(97,123):
    dic[chr(i)] = 0

for i in a:
    dic[i] += 1

ans = 0
alen = len(a)

for i in a:
    ans += alen - dic[i]

print(ans//2+1) #ƒIƒŠƒWƒiƒ‹‚ğ‘«‚·
