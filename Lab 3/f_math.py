from random import randint, choice
from eval import calc

x = randint(1,20)
y = randint(1,20)
op = '+'
err = choice([-1, 1, 0, 0, 0])
op = choice(['+','-','*','/'])

res = calc(x, y, op)
res += err

print('{0} {1} {2} = {3}'.format(x, op, y, res))
print('* '*10)
user = input('(Y/N)? ').lower()

# if (err ==0 and user == 'y') or (err != 0 and user == 'n'):
#     print('Yay')
# else:
#     print('Incorrect')

if err == 0:
    if user == 'y':
        print('Yay')
    else:
        print('Incorrect')
else:
    if user == 'n':
        print('Yay')
    else:
        print('Incorrect')
print('* '*10)
