sx,sy,tx,ty = map(int,input().split())

s = []

for i in range(ty-sy):
    s.append("U")
for i in range(tx-sx):
    s.append("R")
for i in range(ty-sy):
    s.append("D")
for i in range(tx-sx):
    s.append("L")
s.append("L")
for i in range(ty-sy+1):
    s.append("U")
for i in range(tx-sx+1):
    s.append("R")
s.append("D")
s.append("R")
for i in range(ty-sy+1):
    s.append("D")
for i in range(tx-sx+1):
    s.append("L")
s.append("U")

print("".join(s))
