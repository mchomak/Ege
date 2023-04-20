for i in range(1000,10000):
    s1=int(str(i)[0])+int(str(i)[1])
    s2=int(str(i)[2])+int(str(i)[3])
    if s1<s2:
        newNum=str(s2)+str(s1)
    else:
        newNum=str(s1)+str(s2)

    if newNum=="173":
        print(i)
        break