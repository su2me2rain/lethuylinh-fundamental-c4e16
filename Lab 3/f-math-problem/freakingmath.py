from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 20)
    y = randint(1, 20)
    op = choice(['+','-'])
    if op == '+':
        result = x+y
    else:
        result = x-y

    err = choice([-1, 1, 0, 0, 0])
    result += err

    return [x, y, op, err, result]

# def check_answer(x, y, op, result, user_choice):
#     ans = True
#     if err == 0:
#         if user_choice != True:
#             ans = False
#     else:
#         if user_choice != False:
#             ans = False
#     print(ans)
#     return ans
