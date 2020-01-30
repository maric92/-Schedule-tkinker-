from tkinter import *
import math
root=Tk()
root.title("Построение")
root.geometry('1000x820')
canvas = Canvas(root, width= 1000, height=820, bg='blue')
# сетка по оси y
for y in range(20):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 3, width=1, fill='#191938')
#  сетка по оси x
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#191938')
#координатная линия x и y
canvas.create_line(10,10, 10,610, width=1, arrow=FIRST, fill='white')
canvas.create_line(10,310 , 1000,310 , width=1, arrow=LAST, fill='white')
w= 0.02
phi= 10
dy=300
A=200
xy = []

for x in range(1000):
    y = math.sin(x*w)
    xy.append(x+phi)
    xy.append(y * A+ dy)

sin_line = canvas.create_line(xy, fill='white')

canvas.pack()
root.mainloop()
