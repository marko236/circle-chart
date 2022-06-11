from turtle import *
from tkinter.messagebox import showinfo as info
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title("Circle chart calculator")
win.resizable(False,False)
def draw():
    a,b=float(e.get()),float(e2.get())
    d=36000/(a*100/b)
    pensize(5)
    pencolor("blue")
    fillcolor("red")
    Turtle()
    hideturtle()
    begin_fill()
    circle(120)
    end_fill()
    pencolor("black")
    fillcolor("blue")
    begin_fill()
    circle(120,d)
    left(90)
    forward(120)
    left(180-d)
    forward(120)
    end_fill()
    up()
    forward(100)
    down()
    color('red')
    write("FULL SIZE",font=('Monospace',12,'bold'))
    up()
    left(90)
    forward(150)
    right(90)
    color('blue')
    write('PART',font=('Monospace',12,'bold'))
    info(title="RESULT",message=str(round(d,2))+'°')
    bye()

Label(win,text="Full number: ").grid(row=0,column=0)
Label(win,text='Part to show: ').grid(row=1,column=0)
e=Entry(win)
e2=Entry(win)
e.grid(row=0,column=1)
e2.grid(row=1,column=1)
Label(win,text="\n\n").grid(row=2,column=0)
Button(win,text="Evaluate",command=draw).grid(row=3,column=1)
Button(win,text="EXIT",command=exit).grid(row=3,column=0)
win.mainloop()