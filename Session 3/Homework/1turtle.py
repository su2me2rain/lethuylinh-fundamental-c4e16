from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
side = 2
for i in range(len(colors)):
    side = side + 1
    color(colors[i])
    for j in range(side):
        forward(100)
        angle = 360/side
        left(angle)
mainloop()
