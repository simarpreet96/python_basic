import tkinter
from tkinter import *
import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2, n3):  
	num1 = (n1.get())  
	num2 = (n2.get()) 
	num3 = (n3.get()) 
	result = int(num1)+int(num2)+int(num3)  
	label_result.config(text="Result = %d" % result)  
	return 

def toclr():
    entryRef.delete(first=0,last=100)
    entryNum1.delete(first=0,last=100)
    entryNum2.delete(first=0,last=100)
    entryNum3.delete(first=0,last=100)

def toext():
	top.destroy()

top = Tk()
top.geometry('514x358') 
top.title('Billing System')

leftframe = Frame(top, bd = 10, bg = 'light yellow')

number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar() 
ref = tk.StringVar() 

labelNum1 = Label(leftframe, bg='light yellow',text="Refrence").pack()
labelNum1 = Label(leftframe, bg='light yellow', text="P1").pack()
labelNum2 = Label(leftframe, bg='light yellow',text="P2").pack()
labelNum1 = Label(leftframe, bg='light yellow',text="P3").pack()

entryRef = Entry(leftframe, textvariable=ref)
entryRef.pack()
entryNum1 = Entry(leftframe, textvariable=number1)
entryNum1.pack()
entryNum2 = Entry(leftframe, textvariable=number2)
entryNum2.pack()
entryNum3 = Entry(leftframe, textvariable=number3)
entryNum3.pack()

leftframe.pack(side=LEFT)

rightframe = Frame(top, bd = 10, bg = 'light green')


rightframe.pack(side=RIGHT)

bottomframe = Frame(top, bd = 10, bg = 'light pink')

labelResult = tk.Label(bottomframe, bg='light pink')  
labelResult.pack()

call_result = partial(call_result, labelResult, number1, number2, number3)

buttonCal = tk.Button(bottomframe,text="Total", command=call_result).pack() 

buttonclear = tk.Button(bottomframe, text="Clear", command=toclr).pack()

buttonexit = tk.Button(bottomframe, text="Exit", command=toext).pack()

bottomframe.pack(side=BOTTOM)


top.mainloop() 