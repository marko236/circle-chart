try:
    from turtle import *
    from tkinter.messagebox import showinfo as info
    from tkinter import *
    from tkinter.ttk import *
except ImportError:
    print("CCC requires Python 3.x to run")
win=Tk()
win.title("Circle chart calculator")
win.resizable(False,False)
def draw():
    a=round(float(eval(e.get())),2)
    if '%' in e2.get():
        b=round(a*(float(eval(e2.get()[:-1]))/100),2)
    else:
        b=round(float(eval(e2.get())),2)
    d=36000/(a*100/b)
    pensize(5)
    pencolor("blue")
    fillcolor("red")
    Turtle()
    hideturtle()
    begin_fill()
    circle(180)
    end_fill()
    pencolor("black")
    fillcolor("blue")
    begin_fill()
    circle(180,d)
    left(90)
    forward(180)
    left(180-d)
    forward(180)
    end_fill()
    up()
    forward(100)
    down()
    info(title="RESULT",message=(str(round(d,2))+"°\n{}%\n{}".format(b*100/a,b)))
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
