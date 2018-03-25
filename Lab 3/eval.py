from random import randint, choice
#
# # x = float(input('x = '))
# x = 3
# op = choice (['+','-','*','/'])
# # y = float(input('y = '))
# y = 7
#
# result = 0
#
# if op == '+':
#     result = x+y
# elif op == '-':
#     result = x-y
# elif op == '*':
#     result = x*y
# else:
#     result = x/y
#
# print(result)
def calc(x, y, op):
    # op = choice (['+','-','*','/'])
    if op == '+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    else:
        result = x/y
    return result

# argument, parameter
# res = calc(4, 8, '+')
# print(res)
