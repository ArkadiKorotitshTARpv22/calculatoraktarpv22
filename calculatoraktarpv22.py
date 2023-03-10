from math import sqrt
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
def lahenda():
    if a.get()=="" :
        a.configure(bg="red") 
    else:
        a.configure(bg="lightblue")
    if b.get()=="" :
        b.configure(bg="red") 
    else:
        b.configure(bg="lightblue")
    if c.get()=="" :
        c.configure(bg="red")
    else:
        c.configure(bg="lightblue")
    if a.get()!="" and b.get()!="" and c.get()!="":
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_ 
        if D>0:
            x1=round((-b_-sqrt(D))/(2*a_),2)
            x2=round((-b_+sqrt(D))/(2*a_),2) 
            vas=f"X1={x1} \nX2={x2}"
        elif D==0:
            x1=round(-1*b-sqrt(D),2)
            vas=f"X1={x1}" 
        else:
            vas="Lahendust pole"
        vastus.configure(text=vas)
def graafik():
    a_=float(a.get())
    b_=float(b.get())
    c_=float(c.get()) 
    x0=(-b_)/2*a_ 
    y0=a_*x0*x0+b_*x0+c_ 
    x=np.arange(x0-15,x0+15,1)
    y=a_*x*x+b_*x+c_ 
    fig=plt.figure() 
    plt.plot(x,y,'r-d') 
    plt.title("Ruutvõrrand")
    plt.ylabel('Y') 
    plt.xlabel('X') 
    plt.grid(True) 
    plt.show()

aken=Tk()
aken.geometry("650x260")
aken.title("CalculatorRoot")
f1=Frame(aken,width=650,height=260)
f1.pack(side=TOP) 
f2=Frame(aken,width=650,height=260)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="Rootvõrrandite lahendamine", font="Calibri 26",fg="green", bg="lightblue")
lbl.pack(side=TOP) 
vastus=Label(f1,text="Решение",height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)
x2=Label(f1,text="x**2", font="Calibri 26", fg="green", padx=10)
x2.pack(side=LEFT)
b=Entry(f1, font="Calibri 26", fg="green", bg="lightblue",width=3)
