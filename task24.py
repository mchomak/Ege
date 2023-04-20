f = open ('for24.1.txt')
max_len = 0
for s in f:
    if s.count('c') < 30:
        for i in range (len(s)):
            max_len = max(max_len, s.rindex(s[i]) - s.index(s[i]))
print(max_len)

# s.rindex('x') – выдаст последний индекс вхождения 'x' в строку s
# s.index('x') – выдаст первый индекс вхождения 'x' в строку s

