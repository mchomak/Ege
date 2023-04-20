
def Win1(s):
    return ((s+n)>=150 or (s*m-2)>=150)

data=[]
n=2
m=3
# если ход неудачный то мы ставим "or", а если при любом ходе апонента, то мы пишем "and"
for s in range(1,150):
    if Win1(s+n) and Win1(s*m-2):
        data.append(s)

print(min(data))