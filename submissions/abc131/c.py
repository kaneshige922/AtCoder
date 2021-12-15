a,b,c,d = map(int,input().split())

def gcd(a,b): #ユークリッド互除法
    if a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b,r)

gcdcd = c*d//gcd(c,d)

am = a-1

amade = am-(am//c + am//d - am//gcdcd)
bmade = b - (b//c + b//d - b//gcdcd)

print(bmade-amade)
