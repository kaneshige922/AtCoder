import math

n = int(input())
xy0 = list(map(int,input().split()))
xy2 = list(map(int,input().split()))
c = [(xy0[0]+xy2[0])/2,(xy0[1]+xy2[1])/2]
kaku = math.radians(360/n)



xy00 = [xy0[0]-c[0],xy0[1]-c[1]]

ans = [xy00[0]*math.cos(kaku)-xy00[1]*math.sin(kaku),xy00[0]*math.sin(kaku)+xy00[1]*math.cos(kaku)]
ans = [ans[0]+c[0],ans[1]+c[1]]

print(*ans)
