import itertools

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

def kaizyo (i):
    if i != 0:
        return i * kaizyo(i-1)
    else:
        return 1

kumi = list(itertools.permutations([i+1 for i in range(n)]))

a = b = 0

for i in range(kaizyo(n)):
    if list(kumi[i]) == p:
        a = i
    if list(kumi[i]) == q:
        b = i


print(abs(a-b))
