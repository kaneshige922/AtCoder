
n = int(input())

if n >=42: 
    n += 1

n = str(n)

if len(n) == 1:
    print("AGC00"+n)
else:
    print("AGC0"+n)
