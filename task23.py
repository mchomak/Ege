from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

@lru_cache(None)
def task(start,end):
    if start>end:
        return 0
    elif start==end:
        return 1
    else:
        return task(start+2,end)+task(start+3,end)+task(start*3,end)

b1=task(1,5)
b2=task(5,35)
print(b1,b2,b1*b2)