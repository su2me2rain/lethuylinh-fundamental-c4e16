side = 2*int(input('Input the size: '))+1
# print CODE
for i in range(side):
    if i==0 or i==side-1:
        for j in range(side):
            print("* ", end=(''))
        print(' ',end=(''))
        for j in range(side):
            print("* ", end=(''))
        print(' ',end=(''))
        for j in range(int(side/2)+1):
            print("* ", end=(''))
        for j in range(side - int(side/2)-1):
            print('  ', end=(''))
        print(' ',end=(''))
        for j in range(side):
            print("* ", end=(''))
        print()
    elif i==int(side/2):
        print('* ',end=(''))
        for j in range(side-1):
            print('  ', end=(''))
        print(' ', end=(''))
        for f in range(2):
            for j in range(side):
                if j==0 or j==side-1:
                    print('* ',end=(''))
                else:
                    print('  ',end=(''))
            print(' ', end=(''))
        for j in range(int(side/2)+1):
            print('* ',end=(''))
        for j in range(side-int(side/2)-1):
            print('  ', end=(''))
        print()
    else:
        #C
        print('* ', end=(''))
        for j in range(side-1):
            print('  ', end=(''))
        print(' ', end=(''))
        #O
        for j in range(side):
            if j==0 or j==side-1:
                print('* ', end=(''))
            else:
                print('  ', end=(''))
        print(' ', end=(''))
        #D
        if i<int(side/2):
            for j in range(side):
                if j==0 or j==side-1 + i - int(side/2):
                    print('* ', end=(''))
                else:
                    print('  ', end=(''))
            print(' ', end=(''))
        else:
            for j in range(side):
                if j==0 or j==side-1 - i + int(side/2):
                    print('* ', end=(''))
                else:
                    print('  ', end=(''))
            print(' ', end=(''))
        #E
        print('*')
