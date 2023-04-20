file=open("27.1.B.txt","r")
n=int(file.readline())
a=[1,1,2,4]
for i in range(4,n+1):
    a.append(a[i-1] + a[i-2] + a[i-3] + a[i-4])

print(a)