from turtle import *
speed(-1)
color('blue')
n = 30
left(180)
for i in range(45):
    for j in range(4):
        forward(n)
        right(90)
    left(360/40)
    n +=5
mainloop()
