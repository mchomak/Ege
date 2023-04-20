def Del(n,m):
    return n%m==0

mas=[]
for a in range(1,1000):
    flag1=True
    for x in range(1,1000):
        if ((Del(x,87) and (not Del(x,11)))<= (not Del(x,a)))==False:
            flag1=False
            break
    if flag1:
        mas.append(a)

print(mas)
