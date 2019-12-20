import tkinter
from tkinter import *
import tkinter as tk

def toclr():
    entryRef.delete(first=0,last=100)
    entryNum1.delete(first=0,last=100)
    entryNum2.delete(first=0,last=100)
    entryNum3.delete(first=0,last=100)


top = Tk()
top.geometry('514x358') 
top.title('Billing System')

number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar() 
ref = tk.StringVar() 

entryRef = Entry(textvariable=ref).pack()
entryNum1 = Entry(textvariable=number1).pack()
entryNum2 = Entry(textvariable=number2).pack()
entryNum3 = Entry(textvariable=number3).pack()

buttonclear = tk.Button(text="Clear", command=toclr).pack()

top.mainloop()