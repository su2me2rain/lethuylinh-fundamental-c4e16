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
    display_result = result + err
    return [x, y, op, display_result]

def check_answer(x, y, op, display_result, user_choice):
    ans = True
    if op == '+':
        result = x+y
    else:
        result = x-y
    if display_result == result:
        if user_choice != True:
            ans = False
    else:
        if user_choice != False:
            ans = False
    print(ans)
    return ans
