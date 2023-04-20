s="2"*99
while (s.count("999")>=1) or (s.count("222")>=1):
    print(s)
    if "222" in s:
        s=s.replace("222","9",1)
    else:
        s=s.replace("999","2",1)

print(s)