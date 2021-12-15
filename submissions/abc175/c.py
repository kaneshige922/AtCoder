x,k,d = map(int,input().split())


x = abs(x)
if x - k*d >= d:
    print(x-k*d)
else:
    if k % 2 == 0:
        print(abs(x-2*d*((x-d)//(2*d)+1)))
    else:
        print(abs(x-d-2*d*((x-2*d)//(2*d)+1)))
