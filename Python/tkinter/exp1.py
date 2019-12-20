import tkinter
import tkinter as tk 
from functools import partial
import socket
from socket import socket
from socket import *
from tkinter import *

def sum(resultlb, n1,n2):
	num1 =(n1.get())  
	num2 =(n2.get()) 
	result =int(num1)+int(num2)  
	resultlb.config(text="Result = %d" % result)  
	return

def sub(resultlb, n1,n2):
	num1 =(n1.get())  
	num2 =(n2.get()) 
	result =int(num1)-int(num2)  
	resultlb.config(text="Result = %d" % result)  
	return

def mul(resultlb, n1,n2):
	num1 =(n1.get())  
	num2 =(n2.get()) 
	result =int(num1)*int(num2)  
	resultlb.config(text="Result = %d" % result)  
	return

def div(resultlb, n1,n2):
	num1 =(n1.get())  
	num2 =(n2.get()) 
	result =int(num1)/int(num2)  
	resultlb.config(text="Result = %d" % result)  
	return

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

right = Label(m1, text="l ", bg = 'light pink')

top = Tk()
top.geometry('500x500') 
top.title('Billing System') 

buttonCal = tk.Button(top, text="Sum", command=sum).grid(row=3, column=0)
buttonCal = tk.Button(top, text="Sub", command=sub).grid(row=3, column=1)
buttonCal = tk.Button(top, text="Mul", command=mul).grid(row=3, column=2)
buttonCal = tk.Button(top, text="div", command=div).grid(row=3, column=3) 

m1.add(right)

top = Label(m2, text="t", bg = 'light green')

number1 = tk.StringVar()  
number2 = tk.StringVar()  

labelNum1 = tk.Label(top, text="A").grid(row=1, column=0)  
  
labelNum2 = tk.Label(top, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(top)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(top, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(top, textvariable=number2).grid(row=2, column=2)  

sum = partial(sum, labelResult, number1, number2)
sub = partial(sub, labelResult, number1, number2)
mul = partial(mul, labelResult, number1, number2)
div = partial(div, labelResult, number1, number2)

m2.add(top)

bottom = Label(m2, text="b", bg = 'light blue')
m2.add(bottom)

mainloop()

top.mainloop()  