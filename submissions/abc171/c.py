n = int(input())

alp = [chr(i) for i in range(97,123)]
na =[]
name = []
for i in range(1,12):
    na.append((n-1) % 26)
    n = (n-((n-1) % 26)) //26
    if n == 0:
        break
na.reverse()
for i in range(len(na)):
        name.append(alp[na[i]])
print("".join(name))
