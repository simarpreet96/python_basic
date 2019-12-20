import tkinter
from tkinter import *
import tkinter as tk
from functools import partial
import math


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
top.geometry('575x367') 
top.title('Billing System')

#topFrame = Frame(top, width=50, height=40, padx=3, pady=2)

leftframe = Frame(top, bd = 10, bg = '#E8F470')

labelNum1 = Label(leftframe, bg='#E8F470', text="Entry",font="lucida 12 bold").grid(row=0, column=1)
labelNum1 = Label(leftframe, bg='#E8F470', text="").grid(row=0, column=2)

number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar() 
ref = tk.StringVar() 
labelNum1 = Label(leftframe, bg='#E8F470',text="Refrence",font ="Chilanka 12 bold").grid(row=1, column=0)
labelNum1 = Label(leftframe, bg='#E8F470', text="P1",font ="Chilanka 12 bold").grid(row=2, column=0) 
labelNum2 = Label(leftframe, bg='#E8F470',text="P2",font ="Chilanka 12 bold").grid(row=3, column=0)
labelNum1 = Label(leftframe, bg='#E8F470',text="P3",font ="Chilanka 12 bold").grid(row=4, column=0)

entryRef = Entry(leftframe, textvariable=ref,foreground = 'green', font="Chilanka")
entryRef.grid(row=1, column=2)
entryNum1 = Entry(leftframe, textvariable=number1,foreground = 'green', font="Chilanka")
entryNum1.grid(row=2, column=2)
entryNum2 = Entry(leftframe, textvariable=number2,foreground = 'green', font="Chilanka")
entryNum2.grid(row=3, column=2)
entryNum3 = Entry(leftframe, textvariable=number3,foreground = 'green', font="Chilanka")
entryNum3.grid(row=4, column=2)

labelNum1 = Label(leftframe, bg='#E8F470',text='').grid()
labelNum1 = Label(leftframe, bg='#E8F470',text='').grid()
labelNum1 = Button(leftframe, bg='#B7B70D',text='Clear',font ="Chilanka 12 bold",command = toclr ).grid(row=6, column=1)
labelNum1 = Label(leftframe, bg='#E8F470',text='').grid()
labelNum1 = Label(leftframe, bg='#E8F470',text='').grid()
labelNum1 = Label(leftframe, bg='#E8F470',text='').grid()

leftframe.grid( row = 1,column = 0, rowspan = 2, columnspan=1) 

rightframe = Frame(top, bd = 10, bg = 'light green')

labelNum1 = Label(rightframe, bg='light green',text="Calculator",font="lucida 12 bold").grid(row=0, column=0)

inpvalue = StringVar()
inpvalue.set("")
screen = Entry(rightframe, textvar=inpvalue,bd=5, foreground = 'green', font="Chilanka" )
screen.grid()

f = Frame(rightframe, bg='green')
b = Button(f, text="9", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8",bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="green")
b = Button(f, text="6",bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()


f = Frame(rightframe, bg="green")
b = Button(f, text="3", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="1",bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

f = Frame(rightframe, bg="green")

b = Button(f, text=" +",bg='#BB8FCE', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" 0",bg='light blue', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" -",bg='#BB8FCE', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

f = Frame(rightframe, bg="green")

b = Button(f, text=" *",bg='#33FFB5', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/",bg='#33FFB5', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%",bg='#33FFB5', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

f = Frame(rightframe, bg="green")
b = Button(f, text="C",bg='orange', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=" .",bg='#33FFB5', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=",bg='orange', height=1, width=1,font ="Chilanka 12 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.grid()

rightframe.grid(column = 2, row=0, rowspan=2, columnspan=1)

bottomframe = Frame(top, bd = 10, bg = 'light pink',relief="groove")

labelhead = Label(bottomframe, bg='light pink',text="Total,Exit and Clear",font ="lucida 12 bold").grid(row=0,column=1)


labelResult = Label(bottomframe, bg='light pink',foreground = 'green')  
labelResult.grid(row=2, column=1)
call_result = partial(call_result, labelResult, number1, number2, number3)
labelNum1 = Label(bottomframe, bg='light pink',text='',relief="ridge").grid(row=3,column=1)
buttonCal = tk.Button(bottomframe,text="Total", command=call_result,bg='#F178A2',font ="Chilanka 12 bold").grid(row=3, column=0) 

buttonclear = tk.Button(bottomframe, text="Clear", command=toclr,bg='#F178A2',font ="Chilanka 12 bold")
buttonclear.grid(row=3, column=1)
buttonclear.bind("<Button-1>", click)
buttonexit = tk.Button(bottomframe, text="Exit", command=toext,bg='#F178A2',font ="Chilanka 12 bold").grid(row=3, column=2)

bottomframe.grid(row = 3, rowspan=4, columnspan = 3)


#topFrame.grid(row=4, column=2)

top.mainloop()  