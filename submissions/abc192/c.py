n,k = map(int,input().split())
def fx (a):
    t = list(str(a))
    t = [ int(i) for i in t]
    g1 = sorted(t,reverse=True)
    g2 = reversed(g1)
    g1 = [str(i) for i in g1]
    g2 = [str(i) for i in g2]
    fv = int("".join(g1)) - int("".join(g2))
    return fv
for i in range(k):
    n = fx(n)
print(n)
