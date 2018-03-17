value = list(input('Enter your balance: '))

#strip0atthebeginning
c = 0
for i in value:
    if i == '0':
        c += 1
    else:
        break
for i in range(c):
    value.remove('0')

#print
k = len(value) % 3
for i in range(len(value)):
    print(value[i], sep='', end='')
    if (i+1) != len(value):
        if (i+1-k) % 3 == 0:
            print(',',sep='',end='')
print()
