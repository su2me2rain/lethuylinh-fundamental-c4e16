#1
def helloworld():
    for i in range(3):
        print('Hello World')

#2
def sumxy(x,y):
    print(x+y)

#3
from turtle import *
def draw_square(length, colour):
    color(colour)
    speed(-1)
    for j in range(4):
        forward(10*(float(length)+1))
        left(90)
    if i == 29:
        mainloop()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
