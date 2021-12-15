from itertools import permutations

s = list(input())

a = set(list(permutations(s)))

print(len(a))

