# это вариант с 2 кучами камней
def Win1(x,s):
    return (x+n + s)>=251  or (x*m + s)>=251  or (x+s+n)>=251  or (x+s*m)>=251

def Loss1(x,s):
    return ((not(Win1(x,s))) and Win1(x,s + n) and Win1(x,s * m) and Win1(x+n, s) and Win1(x*m,s))

def Win2(x,s):
    return (Loss1(x,s + n) or Loss1(x,s * m) or Loss1(x+n,s) or Loss1(x*m,s))

def Loss12(x,s):
    return ((Win1(x+n,s) or Win2(x+n,s)) and (Win1(x*m, s) or Win2(x*m,s)) and (Win1(x,s+n) or Win2(x,s+n)) and (Win1(x,s*m) or Win2(x,s*m))
            and (Win2(x + n, s) or Win2(x, s + n) or Win2(x * m, s) or Win2(x, s * m)))

data=[]
x=8
n=3
m=4
for s in range(1,242):
    if Loss12(x,s):
        data.append(s)

print(data)