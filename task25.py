def FindDel(number):
    delitely=[]
    for i in range(2,int(number**0.5) + 1):
        if number%i==0:
            delitely.append(i)
    return delitely

count=0

for i in range(320000,100000000000000):
    buf=FindDel(i)
    if len(buf)>0:
        del1=buf[-1]
        if len(FindDel(del1))==0:
            print(i,del1)
            count+=1
    if count==6:
        break
