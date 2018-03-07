from turtle import *
side=float(input("What is the square side?"))
fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(side*10)
    left(90)
end_fill()
mainloop()
