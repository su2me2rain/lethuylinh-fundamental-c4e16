from random import *
from inside import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

meaning = ['BLUE', 'RED', 'GREEN', 'YELLOW']
color = ['#3F51B5', '#FFD600', '#C62828', '#4CAF50']

def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(meaning),
                choice(color),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    result = True
    for k in shapes:
        check = is_inside([x, y], k['rect'])
        if check == True:
            choose_text = k['text']
            choose_color= k['color']
            break
        else:
            check = False
    if check == True:
        if quiz_type == 0:
            if choose_text != text.lower():
                result = False
        else:
            if choose_color != color:
                result = False
    else:
        print("No selection")
        result = False
    return result
