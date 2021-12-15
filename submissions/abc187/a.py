a,b = input().split()
asum = bsum = 0
for i in range(3):
  asum += int(a[i])
  bsum += int(b[i])
print(max(asum,bsum))
