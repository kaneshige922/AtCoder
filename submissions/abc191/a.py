v,t,s,d = map(int,input().split())
a = d/v
if t <= a and a <= s:
  print("No")
else:
  print("Yes")
