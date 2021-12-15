n = 1048576 
#n = 100#—v‘f”n‚ğéŒ¾
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            #if self.size[a] < self.size[b]:
            #    a, b = b, a

            self.num_sets -= 1
            self.parent[a] = b
            #self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets



q = int(input())
queri = [list(map(int,input().split())) for i in range(q)]
L = [-1]*n

v = set()
UF = DisjointSetUnion(n)
for i in range(q):
    t = queri[i][0]
    x = queri[i][1]
    if t == 1:
        h = x % n
        if h in v:
            h = UF.find(h)
            UF.union(h,UF.find((h+1)%n))
            L[h] = x
            v.add(h)
        else:
            UF.union(h,UF.find((h+1)%n))
            #print(UF.find(h))
            v.add(h)
            L[h] = x
    else:
        print(L[x%n])
