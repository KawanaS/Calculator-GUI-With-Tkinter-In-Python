from tkinter import*
from tkinter import messagebox

root=Tk()
root.title('Calculator')
root.configure(background='light blue')

frame1=LabelFrame(root,text='',pady=5,padx=5)
frame1.pack(padx=10,pady=10)

frame2=LabelFrame(root,text='',pady=5,padx=5)
frame2.pack(padx=10,pady=10)

e=Entry(frame1,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,pady=40,padx=40)

def click(number):
      current=e.get()
      e.delete(0, END)
      e.insert(0,str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_num=e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_num)
    e.delete(0, END)


def subtract():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)


def divide():
    first_num = e.get()
    global f_num

    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0, END)


def multiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0, END)
def sqroot():
    first_num = e.get()
    global f_num
    global math
    math = 'sqrt'
    f_num = int(first_num)
    e.delete(0, END)

def quit():
    if messagebox.askyesno("EXIT", "Do you want to exit?"):
        root.destroy()
def equal():
    second_num=e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, f_num + float(second_num))

    if math == 'subtraction':
        e.insert(0, f_num - float(second_num))

    if math == 'multiplication':
        e.insert(0, f_num * float(second_num))

    if math == 'division':
        e.insert(0, f_num / float(second_num))
    if math=='sqrt':
        e.insert(0,f_num**0.5)

#define buttons
button_quit=Button(frame2,text='Exit',pady=10,padx=20,bg='red',command=quit)
button_quit.grid(row=1,column=0,columnspan=3)
button1=Button(frame2,text='1',padx=60,pady=20, bg='green',command=lambda: click(1))
button1.grid(row=4,column=0)
button2=Button(frame2,text='2',padx=60,pady=20, bg='yellow',command=lambda: click(2))
button2.grid(row=4,column=1)
button3=Button(frame2,text='3',padx=60,pady=20, bg='green',command=lambda: click(3))
button3.grid(row=4,column=2)
button4=Button(frame2,text='4',padx=60,pady=20, bg='yellow',command=lambda:click(4))
button4.grid(row=3,column=0)
button5=Button(frame2,text='5',padx=60,pady=20, bg='green',command=lambda:click(5))
button5.grid(row=3,column=1)
button6=Button(frame2,text='6',padx=60,pady=20, bg='yellow',command=lambda:click(6))
button6.grid(row=3,column=2)
button7=Button(frame2,text='7',padx=60,pady=20, bg='orange',command=lambda:click(7))
button7.grid(row=2,column=0)
button8=Button(frame2,text='8',padx=60,pady=20, bg='yellow',command=lambda:click(8))
button8.grid(row=2,column=1)
button9=Button(frame2,text='9',padx=60,pady=20, bg='orange',command=lambda:click(9))
button9.grid(row=2,column=2)
button0=Button(frame2,text='0',padx=60,pady=20, bg='green',command=lambda:click(0))
button0.grid(row=5,column=1)
button_add=Button(frame2,text='+',padx=60,pady=20,command=add)
button_add.grid(row=5,column=0)
button_equal=Button(frame2,text='=',padx=60,pady=20,command=equal)
button_equal.grid(row=5,column=2)
button_clear=Button(frame2,text='Clear',padx=60,pady=20, bg="red",command=clear)
button_clear.grid(row=7,column=1)
sqrt_button=Button(frame2,text='√',padx=60,pady=20,command=sqroot)
sqrt_button.grid(row=7,column=0)
pi_button=Button(frame2,text='π',padx=60,pady=20,command=lambda:click(3.142))
pi_button.grid(row=7,column=2)
button_subtract = Button(frame2, text="-", padx=60, pady=20, command=subtract)
button_subtract.grid(row=6, column=0)
button_multiply = Button(frame2, text="X", padx=60, pady=20, command=multiply)
button_multiply.grid(row=6, column=1)
button_divide = Button(frame2, text="÷", padx=61, pady=20, command=divide)
button_divide.grid(row=6, column=2)

root.mainloop()