# это вариант с 2 кучами камней
def Win1(x,s):
    return (x+n + s)>=251  or (x*m + s)>=251  or (x+s+n)>=251  or (x+s*m)>=251

def Loss1(x,s):
    return ((not(Win1(x,s))) and Win1(x,s + n) and Win1(x,s * m) and Win1(x+n, s) and Win1(x*m,s))

def Win2(x,s):
    return (Loss1(x,s + n) or Loss1(x,s * m) or Loss1(x+n,s) or Loss1(x*m,s))

data=[]
# если ход неудачный то мы ставим "or", а если при любом ходе апонента, то мы пишем "and"
x=8
n=3
m=4
for s in range(1,242):
    if Win2(x,s):
        data.append(s)

print(data)