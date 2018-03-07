n = int(input('Input a number: '))
for i in range(n):
    for j in range(n):
        k = (i+1)*(j+1)
        print(k, end = ' ')
        if k<10:
            print('  ', end='')
        elif k<100:
            print(' ', end='')
    print('')
