"""
" author : kaneshige
" created : 21.12.2021 00:25:47
"""

import sys
import itertools
from collections import deque,defaultdict
from copy import deepcopy
from heapq import heappop,heappush


def main():
    n = int(readline())
    XYZ = [list(map(int,readline().split())) for _ in range(n)]
    dic = {}

    s = (0,0) #訪問済み、最後、距離
    dic[s] = 0

    def dis(a,b):
        result = abs(XYZ[a][0]-XYZ[b][0]) + abs(XYZ[a][1]-XYZ[b][1]) + max(0,XYZ[a][2]-XYZ[b][2])
        return result

    dist1 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist1[i][j] = dis(j,i)

    """
    三角不等式よりダイクストラ不要（2点間の移動に経由する点はなし）
    dist2 = []
    for i in range(n):
        dist = [float("inf")] * n
        #parents = [-1] * n
        dist[i] = 0

        queue = [(0,i)]

        while queue:
            path_len, v = heappop(queue)
            for j in range(n):
                if dist1[v][j] + path_len < dist[j]:
                    dist[j] = dist1[v][j] + path_len
                    #parents[j] = v
                    heappush(queue, (dist1[v][j] + path_len, j))
        dist2.append(dist)
        """

    dist2 = dist1

    for i in range(1,n):
        dic2 = {}
        for p in dic:
            p1 = p[0]
            last = p[1]
            for j in range(1,n):
                if not(p1 >> j & 1):
                    p3 = p1 + 2**j
                    if (p3,j) in dic2:
                        dic2[(p3, j)] = min(dic2[(p3, j)],dic[p] + dist2[last][j])
                    else:
                        dic2[(p3,j)] = dic[p] + dist2[last][j]
        dic = deepcopy(dic2)

    ans = INF

    for i in dic:
        ans = min(ans,dic[i]+dist2[i[1]][0])


    #print(dic)
    print(ans)









if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
