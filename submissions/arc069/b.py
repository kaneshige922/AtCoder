"""
" author : kaneshige
" created : 03.03.2022 17:31:11
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    s = readline().rstrip()

    def end(x):
        fa = []
        for i in x:
            if i:
                fa.append("W")
            else:
                fa.append("S")
        print("".join(fa))
        exit()



    for i in range(4):
        ans = [-1] * n
        for j in range(2):
            if i >> j & 1:
                ans[j] = False
            else:
                ans[j] = True
        t = True
        for j in range(n):
            #print(ans)
            if j == 0:
                if ans[j]:
                    if s[j] == "o":
                        ans[-1] = not(ans[j+1])
                    else:
                        ans[-1] = ans[j+1]
                else:
                    if s[j] == "o":
                        ans[-1] = ans[j+1]
                    else:
                        ans[-1] = not(ans[j+1])
            elif j == n-2:
                if ans[j]:
                    if s[j] == "o" and ans[j-1] == ans[j+1]:
                        break
                    if s[j] == "x" and ans[j-1] != ans[j+1]:
                        break
                else:
                    if s[j] == "o" and ans[j-1] != ans[j+1]:
                        break
                    if s[j] == "x" and ans[j-1] == ans[j+1]:
                        break
            elif j == n-1:
                if ans[j]:
                    if s[j] == "o" and ans[j-1] != ans[0]:
                        end(ans)
                    if s[j] == "x" and ans[j-1] == ans[0]:
                        end(ans)
                else:
                    if s[j] == "o" and ans[j-1] == ans[0]:
                        end(ans)
                    if s[j] == "x" and ans[j-1] != ans[0]:
                        end(ans)
            else:
                if ans[j]:
                    if s[j] == "o":
                        ans[j+1] = not(ans[j-1])
                    else:
                        ans[j+1] = ans[j-1]
                else:
                    if s[j] == "o":
                        ans[j+1] = ans[j-1]
                    else:
                        ans[j+1] = not(ans[j-1])

    print(-1)

if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
