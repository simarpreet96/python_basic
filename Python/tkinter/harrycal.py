
from tkinter import *

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

    else:
        inpvalue.set(inpvalue.get() + text)
        screen.update()

top = Tk()
top.geometry("644x970")
top.title("Calculator By CodeWithHarry")

inpvalue = StringVar()
inpvalue.set("")
screen = Entry(top, textvar=inpvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(top, bg="grey")
b = Button(f, text="9", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(top, bg="grey")
b = Button(f, text="6", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(top, bg="grey")
b = Button(f, text="3", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(top, bg="grey")
b = Button(f, text="0", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(top, bg="grey")
b = Button(f, text="/", padx=33, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=21, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=27, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(top, bg="grey")
b = Button(f, text="C", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

top.mainloop()
