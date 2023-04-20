# это вариант с 2 кучами камней
def Win1(x,s):
    return (x+n + s)>=251  or (x*m + s)>=251  or (x+s+n)>=251  or (x+s*m)>=251

data=[]
# если ход неудачный то мы ставим "or", а если при любом ходе апонента, то мы пишем "and"
x=8
n=3
m=4
for s in range(1,242):
    if Win1(x,s+4) and Win1(x,s*2) and Win1(x+4,s) and Win1(x*2,s):
        data.append(s)

print(data)