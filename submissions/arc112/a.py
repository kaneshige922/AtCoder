t = int(input())
lr = [list(map(int,input().split())) for i in range(t)]

def q(l,r):
    if 2*l > r:
        return 0
    else:
        a = r - 2*l
        ans = (a+1)*(a+2)//2
        return ans

for i in lr:
    print(q(i[0],i[1]))
