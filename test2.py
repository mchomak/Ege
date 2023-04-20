from functools import lru_cache
import sys
sys.setrecursionlimit(1000000000)
cmd=0
num=1

@lru_cache(None)
def task(start,end):
    global num
    global cmd

    if start>end:
        return 0
    elif start==end:
        return 1
    else:
        n=task(start+1,end)
        if cmd==1:
            num+=1
            if num>3:
                return 0
        else:
            num=0
            cmd=1

        n1=task(start*3,end)
        if cmd==2:
            num+=1
            if num>3:
                return 0
        else:
            num=0
            cmd=2

        return n+n1

b=task(1,30)
print(b)