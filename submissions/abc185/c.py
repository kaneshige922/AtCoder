l = int(input())
def kaizyo (n):
    if n != 0:
        return n * kaizyo(n-1)
    else:
        return 1

ans = kaizyo(l-1)//(kaizyo(11)*kaizyo(l-12))

print(ans)
