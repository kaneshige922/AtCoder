n,a,b,c,d = map(int,input().split())
s = list(input())

aok = False
bok = False

while a != c or b != d:
    if c < d:
        if not(bok):
            if b + 2 == d or b+1 == d:
                bok = True
                b = d
            elif b+2 <= n and s[b+1] == ".":
                    b += 2
            elif s[b] == ".":
                b += 1
            else:
                print("No")
                exit()
        else:
            if a+2 == c or a+1 == c:
                aok = True
                a = c
            elif a+2 <= n and s[a+1] == ".":
                    a += 2
            elif s[a] == ".":
                a += 1
            else:
                print("No")
                exit()
    else:
        if not(aok):
            if a+2 == c or a+1 == c:
                aok = True
                a = c
            elif s[a] == "#" and s[a+1] == "#":
                print("No")
                exit()
            elif a+2 <= n and s[a+1] == "." and a+2 != b:
                    a += 2
            elif s[a] == "." and a+1 != b:
                a += 1
            else:
                if not(bok):
                    if s[b] == ".":
                        b += 1
                    elif b+2 <= n and s[b+1] == ".":
                            b += 2
                    else:
                        print("No")
                        exit()
                    if b == d:
                        bok = True
                else:
                    print("No")
                    exit()
        else:
            if b + 2 == d or b+1 == d:
                bok = True
                b = d
            elif b+2 <= n and s[b+1] == ".":
                    b += 2
            elif s[b] == ".":
                b += 1
            else:
                print("No")
                exit()

                

print("Yes")


