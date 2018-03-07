from turtle import *
radius=float(input("What is the circle radius? "))
quantity=int(input("How many circle do you like to draw? "))
angle=360/quantity
fillcolor('green')
begin_fill()
speed(-1)
for i in range(quantity):
    circle(radius*10)
    left(angle)
end_fill()
mainloop()
