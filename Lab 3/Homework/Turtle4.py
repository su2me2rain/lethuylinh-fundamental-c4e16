from turtle import *
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()
    for j in range(5):
        forward(length*10)
        right(144)
    if i == 99:
        mainloop()

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
