item = ['T-Shirt', 'Sweater']
demands = ['c','r','u','d']

demand = input('Welcome to our shop, what do you want (C, R, U, D)? ')
if demand.lower() in demands:
    if demand.lower() == 'c':
        item.append(input('Enter new item: '))

    elif demand.lower() == 'u':
        position = int(input('Update position? '))
        while position > len(item):
            print('Index out of range. Please enter a number smaller than ', len(item),': ')
            position = int(input('Update position? '))
        item[position-1] = input('New item? ')

    elif demand.lower() == 'd':
        position = int(input('Delete position? '))
        while position > len(item):
            print('Index out of range. Please enter a number smaller than ', len(item),': ')
            position = int(input('Update position? '))
        del item[position-1]
        
    print('Our items: ', end='')
    print(*item, sep=', ')
else:
    print('Order is not valid.')
