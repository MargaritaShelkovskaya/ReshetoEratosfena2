n = int(input('n='))
spisok = []
for i in range (2, n + 1):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        spisok.append(i)
print (spisok)
