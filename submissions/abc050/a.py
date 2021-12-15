n = int(input())
a = list(map(int,input().split()))

dic = {}

if n % 2 == 0:
    for i in a:
        if i % 2 == 0:
            print(0)
            exit()
        if i in dic:
            if dic[i] == 1:
                dic[i] += 1
            else:
                print(0)
                exit()
        else:
            dic[i] = 1
    print(2**(n//2) %1000000007)
else:
    for i in a:
        if i % 2 == 1:
            print(0)
            exit()
        if i in dic:
            if i == 0:
                print(0)
                exit()
            elif dic[i] == 1:
                dic[i] += 1
            else:
                print(0)
                exit()
        else:
            dic[i] = 1
    print(2**(n//2) %1000000007)
