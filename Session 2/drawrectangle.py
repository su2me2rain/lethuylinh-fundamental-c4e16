width = int(input('Input the width: '))
length = int(input('Input the length: '))
# stringlength=length*'* '
for i in range(width):
    for j in range(length):
        print('* ', end='')
    print()
