import itertools

s,k = input().split()
k = int(k)
s = list(s)

sl = set(itertools.permutations(s))
sl = list(sl)
sl.sort()

print("".join(sl[k-1]))
