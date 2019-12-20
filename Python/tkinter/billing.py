import tkinter
import tkinter as tk 
from functools import partial
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

#def toclr()


#def toext():
	#top.destroy()

top = Tk()
top.geometry('500x500') 
top.title('Billing System') 

frame = Frame(top)   

  
leftframe = Frame(top, bd = 5, bg = 'light yellow')

number1 = StringVar()  
number2 = StringVar()  

labelNum1 = Label(leftframe, text="P1").grid(row=1, column=0)
  
labelNum2 = Label(leftframe, text="P2").grid(row=2, column=0)
  
entryNum1 = Entry(leftframe, textvariable=number1).grid(row=1, column=2)
  
entryNum2 = Entry(leftframe, textvariable=number2).grid(row=2, column=2)

leftframe.pack(side = LEFT)  

rightframe = Frame(top, bd = 5, bg = 'light green') 

buttonCal = Button(rightframe,  text="Sum", command=sum).grid(row=3, column=0)
buttonCal = Button(rightframe,  text="Sub", command=sub).grid(row=3, column=1)
buttonCal = Button(rightframe,  text="Mul", command=mul).grid(row=3, column=2)
buttonCal = Button(rightframe,  text="Div", command=div).grid(row=3, column=3)

rightframe.pack(side = RIGHT)

bottomframe = Frame(top, bd = 5, bg = 'light pink')  

labelResult = Label(bottomframe,bg='light blue')

labelResult.grid(row=7, column=2)

#Button(bottomframe, text = "clear", command = toclr).pack()

#Button(bottomframe, text = "Exit", command = toext).pack()

bottomframe.pack(side = BOTTOM)

frame.pack()  

top.mainloop()  