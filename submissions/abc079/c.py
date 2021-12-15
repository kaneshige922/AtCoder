num = list(input())
num = [int(i) for i in num]

to = 7 - num[0]
ans = ["+","+","+","="]

for i in range(2**3):
    wa = 0
    for j in range(3):
        if (i >> j) & 1:
            wa += num[j+1]
            ans[j] = "+"
        else:
            wa -= num[j+1]
            ans[j] = "-"
    if wa == to:
        kai = [str(num[0])]
        for j in range(3):
            kai.append(ans[j])
            kai.append(str(num[j+1]))
        kai = kai + ["=","7"]
        print("".join(kai))
        exit()
    

