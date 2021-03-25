'''
CSC 440
bsgs.py
Ximan Liu
'''

from math import ceil, sqrt

def bsgs(p, a, b):
    n = ceil(sqrt(p - 1))
    m = {pow(a, i, p): i for i in range(n)}
    c = pow(a, n * (p - 2), p)
    for j in range(n):
        k = (b * pow(c, j, p)) % p
        if k in m:
            return j * n + m[k]
    return None

print(bsgs(1416545561, 1035, 1369318585))

