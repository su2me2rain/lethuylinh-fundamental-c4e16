from turtle import *
side = 2
for i in range(5):
    side = side + 1
    if side % 2:
        color('blue')
    else:
        color('red')
    for j in range(side):
        forward(100)
        angle = 360/side
        left(angle)
mainloop()
