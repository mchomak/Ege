file = open("27.B.3_dz_1.txt", "r")
n = int(file.readline())
endSum = 0
raznisa = []
for i in file:
    a, b, c = map(int, i.split())
    buf = max(a, b, c) - min(a, b, c)
    if buf != 0 and buf % 49 > 0:
        raznisa.append(max(a, b, c) - min(a, b, c))
    endSum += max(a, b, c)

print(min(raznisa))
print(endSum, endSum % 49)
print(endSum - min(raznisa))
