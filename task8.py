from itertools import *
num=0
for i in permutations("123456789",r=3):
    print(i)
    num+=1
print(num)