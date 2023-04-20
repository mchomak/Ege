import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n<=5:
        return n

    if n>5:
        if n%3==0:
            return n + F(n // 3 + 2)
        else:
            return 0

for n in range(10000):
    b=F(n)
    if b>1100 and b<2000:
        print(b,n)
        break
