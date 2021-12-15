####https://qiita.com/takayg1/items/c811bd07c21923d7ec69 ������p#####
#�o�΃Z�O�����g�؂���肽��
#####segfunc#####
def segfunc(x, y):
    return x^y
#################

#####ide_ele#####
ide_ele = 0
#################

class SegTree:
    """
    init(init_val, ide_ele): �z��init_val�ŏ����� O(N)
    update(k, x): k�Ԗڂ̒l��x�ɍX�V O(N)
    query(l, r): ���[l, r)��segfunc�������̂�Ԃ� O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: �z��̏����l
        segfunc: ��Ԃɂ���������
        ide_ele: �P�ʌ�
        n: �v�f��
        num: n�ȏ�̍ŏ���2�ׂ̂���
        tree: �Z�O�����g��(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # �z��̒l��t�ɃZ�b�g
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # �\�z���Ă���
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k�Ԗڂ̒l��x�ɍX�V
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x   #�X�V�@
        #self.tree[k] += x #���Z
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)��segfunc�������̂𓾂�
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n,q = map(int,input().split())
a = list(map(int,input().split()))
seg = SegTree(a, segfunc, ide_ele)

ans = []

for i in range(q):
    t,x,y = map(int,input().split())
    if t == 1:
        seg.update(x-1,seg.query(x-1,x)^y)
    else:
        ans.append(seg.query(x-1,y))

for i in ans:
    print(i)
