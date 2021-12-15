S = {}
for i in range(4):
    s = input()
    if not(s in S.keys()):
        S[s] = 1
if "H" in S.keys() and "2B" in S.keys() and "3B" in S.keys() and "HR" in S.keys():
    print("Yes")
else:
    print("No")
