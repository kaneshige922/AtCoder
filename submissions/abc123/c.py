import math

n = int(input())
ab = [int(input()) for i in range(5)]

mina = min(ab)

print(4+math.ceil(n/mina))
