from turtle import *
side=float(input("What is the triangle side?"))
fillcolor('yellow')
begin_fill()
for i in range(3):
    forward(side*10)
    left(120)
end_fill()
mainloop()
