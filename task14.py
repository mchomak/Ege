for x in range(100):
    num=int("AB5"+str(x)+"3",18)+int("EF"+str(x)+"13",18)
    if num%17==0:
        print(num/17)
        break