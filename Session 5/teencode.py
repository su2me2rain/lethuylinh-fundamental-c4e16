teencode = {
    'any': 'anh người yêu',
    'eny': 'Em người yêu',
    'dc': 'được',
    'ls': 'làm sao'
}
for key in teencode:
    print(key, end='\t')
print()

while True:
    search = input('Enter code: ')
    if search in teencode:
        print('Code: ', search)
        print('Translation', teencode[search])
    else:
        update = input('Not found. Do you want to contribute this word? (Y/N) ')
        if update.lower() == 'y':
            teencode[search] = input('Enter your translation: ')
            print('Updated')
            for key in teencode:
                print(key, end = '\t')
            print()
        else:
            break
