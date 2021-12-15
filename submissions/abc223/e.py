x,y,a,b,c = map(int,input().split())

def myceil(a,b):
    return a//b + (a%b!=0)


if a+b+c > x*y:
    print("No")
    exit()

#xÅ‘å‚Ü‚Å
Y1 = y- (myceil(a,x)+myceil(b,x)+myceil(c,x))
if Y1 >= 0:
    print("Yes")
    exit()


x1 = x - (myceil(a,y)+myceil(b,y)+myceil(c,y))
if x1 >= 0:
    print("Yes")
    exit()

def tate2yoko(t1,t2,yo):
    Y = y - myceil(yo,x)
    #if Y <= 0:
    #    return False
    X = x - myceil(t1,Y)
    return X*Y >= t2
def tateyoko2(y1,y2,ta):
    X = x - myceil(ta,y)
    #if X <= 0:
    #    return False
    Y = y - myceil(y1,X)
    return X*Y>=y2

if tate2yoko(a,b,c) or tateyoko2(a,b,c):
    print("Yes")
    exit()
if tate2yoko(b,c,a) or tateyoko2(b,c,a):
    print("Yes")
    exit()
if tate2yoko(c,a,b) or tateyoko2(c,a,b):
    print("Yes")
    exit()


print("No")
