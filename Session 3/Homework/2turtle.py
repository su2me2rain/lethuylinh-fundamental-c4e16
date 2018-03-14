from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)
for i in range(len(colors)):
    color(colors[i])
    fillcolor(colors[i])
    begin_fill()
    for j in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    forward (100)
    end_fill()
mainloop()
