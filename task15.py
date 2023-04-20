Q=list(range(12,92))
P=list(range(10,53))
A=[]
# е забываем про общие скобки на всем условии
for x in range(1000):
    if (((x in P) and (x in Q)) <= (x in A))==False:
        A.append(x)
print(A)
# ответом будет не длина а разница максимального и минимального
print(A[-1]-A[0])

