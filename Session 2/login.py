import getpass
user = input('Username: ')
password = getpass.getpass('Password: ')
if user.lower() == 'c4e':
    if password == '123':
        print('Welcome', user)
    else: #!= is unequal
        print('Wrong password')
else:
    print('Username is not available')
