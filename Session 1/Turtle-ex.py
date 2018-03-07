# side=int(input("How many sides of the shape do you want?"))
# print("How many sides of the shape do you want?" )
from turtle import *
shape('turtle')
color('blue')
speed(-1)
fillcolor("green")
begin_fill()
# for i in range(side):
#     forward(100)
#     left(360/side)
for i in range(100):
    # draw a square
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)

    left(7)
end_fill()
mainloop()
