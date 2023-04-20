import math
file=open("for26.1.txt","r")

text79=[]
text80=[]
end=[]
sum1=0
sum2=0
max=0

for i in range(10000):
    stroka=file.readline()
    if len(stroka)>0:
        if int(stroka)>80:
            text80.append(int(stroka))
        else:
            text79.append(int(stroka))

text80.sort(reverse=True)
text79.sort(reverse=True)
numObr=-1
len79=len(text79)
len80=len(text80)

for num in range(0,len80//2):
    end.append(text80[num])
    end.append(text80[numObr])
    sum1=sum1+text80[num]
    sum2=sum2+text80[numObr]
    if text80[numObr]>max:
        max=text80[numObr]
    numObr=numObr-1

end=end+text79
itog=math.ceil(sum1+sum(text79)+sum2*0.55)
print(itog,max)