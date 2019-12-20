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
	
def e1_delete():
    Ref.delete(first=0,last=22)
    Num1.delete(first=0,last=22)
    Num2.delete(first=0,last=22)
    Num3.delete(first=0,last=22)


def toext():
	top.destroy()



def click(event):
	global inpvalue
	text = event.widget.cget("text")
	if text == "=":
		if inpvalue.get().isdigit():
			value = int(inpvalue.get())
		else:
			try:
				value = eval(screen.get())

			except Exception as e:
				print(e)
				value = "Error"


		inpvalue.set(value)
		screen.update()

	elif text == "C":
		inpvalue.set("")
		screen.update()

	elif text == "Clear":
		inpvalue.set("")
		screen.update()

	else:
		inpvalue.set(inpvalue.get() + text)
		screen.update()


top = Tk()
top.geometry('514x358') 
top.title('Billing System')

topFrame = Frame(top, width=50, height=40, padx=3, pady=2)

leftframe = Frame(top, bd = 10, bg = 'light yellow')

labelNum1 = Label(leftframe, bg='light yellow', text="Entry").grid(row=0, column=1)
labelNum1 = Label(leftframe, bg='light yellow', text="").grid(row=0, column=2)

number1 = StringVar()  
number2 = StringVar()
number3 = StringVar() 
ref = StringVar() 
labelNum1 = Label(leftframe, bg='light yellow',text="Refrence").grid(row=1, column=0)
labelNum1 = Label(leftframe, bg='light yellow', text="P1").grid(row=2, column=0) 
labelNum2 = Label(leftframe, bg='light yellow',text="P2").grid(row=3, column=0)
labelNum1 = Label(leftframe, bg='light yellow',text="P3").grid(row=4, column=0)


Ref = Entry(leftframe, textvariable=ref).grid(row=1, column=2)
Num1 =Entry(leftframe, textvariable=number1).grid(row=2, column=2)
Num2 =Entry(leftframe, textvariable=number2).grid(row=3, column=2)
Num3 =Entry(leftframe, textvariable=number3).grid(row=4, column=2)
but = button(leftframe, text="shjkhsk", command=e1_delete ).grid(row=5, column=2)

labelNum1 = Label(leftframe, bg='light yellow',text='').grid()
labelNum1 = Label(leftframe, bg='light yellow',text='').grid()
labelNum1 = Label(leftframe, bg='light yellow',text='').grid()
labelNum1 = Label(leftframe, bg='light yellow',text='').grid()
labelNum1 = Label(leftframe, bg='light yellow',text='').grid()
labelNum1 = Label(leftframe, bg='light yellow',text='').grid()

leftframe.grid( row = 1,column = 0, rowspan = 2, columnspan=1) 

rightframe = Frame(top, bd = 10, bg = 'light green')

labelNum1 = Label(rightframe, bg='light green',text="Calculator").grid(row=0, column=0)

inpvalue = StringVar()
inpvalue.set("")
screen = Entry(rightframe, textvar=inpvalue, font="lucida")
screen.grid()

f = Frame(rightframe, bg="grey")
b = Button(f, text="9", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8",font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="grey")
b = Button(f, text="6", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4",font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="grey")
b = Button(f, text="3", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2",font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="grey")
b = Button(f, text=" 0", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" -", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" *",  font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="grey")
b = Button(f, text="/", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=",font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

f = Frame(rightframe, bg="grey")
b = Button(f, text="C",font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" .", font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" +",  font="lucida")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

rightframe.grid(column = 2, row=0, rowspan=2, columnspan=1)

bottomframe = Frame(top, bd = 10, bg = 'light pink', width=50)

labelNum1 = Label(bottomframe, bg='light pink',text="Total,Exit and Clear").grid(row=0, column=1)
labelResult = tk.Label(bottomframe, bg='light pink')  
labelResult.grid(row=2, column=1)
call_result = partial(call_result, labelResult, number1, number2, number3)
labelNum1 = Label(bottomframe, bg='light pink',text='').grid(row=3,column=1)
buttonCal = tk.Button(bottomframe,text="Total", command=call_result).grid(row=3, column=0) 


#buttonclear = Button(bottomframe, text="Clear")
#buttonclear.grid()
#buttonclear.bind("<Button-1>", click)


buttonexit =Button(bottomframe, text="Exit", command=toext).grid(row=3, column=2)

bottomframe.grid(row = 3, rowspan=4, columnspan = 3)


topFrame.grid(row=4, column=2)

top.mainloop()  