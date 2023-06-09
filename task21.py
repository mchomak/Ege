# функция проверяет возоможно ли выиграть за один ход
def Win1(s):
    return ((s+n)>=winNum or (s*m-2)>=winNum)

# 2. проверяет, является ли текущая позиция проигрышной за 1 ход.
# Проигрышная за 1 ход позиция — это позиция, из которой соперник 100% выиграет, как бы мы ни сходили (причём выиграет своим первым ходом).
def Loss1(S):
    return ((not(Win1(S))) and Win1(S + n) and Win1(S * m-2))

# проверяет, является ли текущая позиция выигрышной за два хода. То есть может ли игрок, который будет из неё ходить, победить своим вторым ходом.
def Win2(S):
    return (Loss1(S + n) or Loss1(S * m-2))

# проверяет, является ли текущая позиция проигрышной за 1 или 2 хода
def Loss12(S):
    return Win2(S+n) and Win1(S*m-2)
# ((Win1(S + 3) or Win2(S + 3)) and (Win1(S * 5) or Win2(S * 5)) and (Win2(S + 3) or Win2(S * 5)))
# более слабьая позиция выигрывается за 2 хода (S+1), а более сильная за 1 ход (S*3)

data=[]
winNum=150
n=2
m=3
for S in range(1, winNum):
    if Loss12(S):
        data.append(S)

print(data)

