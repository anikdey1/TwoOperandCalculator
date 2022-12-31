from tkinter import *

root = Tk()
root.title("Calculator")

# This function defines the operation of button clicks.
def button_click(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))

# This function defines the addition operation.
def button_add():
    if(entry1.get() == ''):
        return
    global first_number
    global arithmetic
    arithmetic = "addition"
    first_number = int(entry1.get())
    entry1.delete(0, END)

# This function defines the subtraction operation.
def button_subtract():
    if(entry1.get() == ''):
        return
    global first_number
    global arithmetic
    arithmetic = "subtraction"
    first_number = int(entry1.get())
    entry1.delete(0, END)

# This function defines the multiplication operation.
def button_multiply():
    if(entry1.get() == ''):
        return
    global first_number
    global arithmetic
    arithmetic = "multiplication"
    first_number = int(entry1.get())
    entry1.delete(0, END)

# This function defines the subtraction operation.
def button_divide():
    if(entry1.get() == ''):
        return
    global first_number
    global arithmetic
    arithmetic = "division"
    first_number = int(entry1.get())
    entry1.delete(0, END)

# This function defines the totaling operation.
def button_total():
    if(entry1.get() == ''):
        return
    second_number = int(entry1.get())
    entry1.delete(0, END)
    if(arithmetic == "addition"):
        entry1.insert(0,((first_number) +(second_number)))
    elif(arithmetic == "subtraction"):
        entry1.insert(0,((first_number) -(second_number)))
    elif(arithmetic == "multiplication"):
        entry1.insert(0,((first_number) *(second_number)))
    elif(arithmetic == "division"):
        entry1.insert(0,((first_number) /(second_number)))

# This function defines the clearing operation.
def button_clear():
    entry1.delete(0, END)

entry1 = Entry(root, width = 35)
entry1.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5, ipady = 25)

# These Tkinter Button objects create the numeric buttons.
button0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: button_click(0))
button1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: button_click(1))
button2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: button_click(2))
button3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: button_click(3))
button4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: button_click(4))
button5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: button_click(5))
button6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: button_click(6))
button7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: button_click(7))
button8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: button_click(8))
button9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: button_click(9))

# These grid() calls place the numeric buttons.
button0.grid(row = 4, column = 1)
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

# These Tkinter Button objects create the operational buttons.
button_plus = Button(root, text = "+", padx = 29, pady = 20, command = button_add)
button_minus = Button(root, text = "-", padx = 30, pady = 20, command = button_subtract)
button_cross = Button(root, text = "×", padx = 29, pady = 20, command = button_multiply)
button_by = Button(root, text = "÷", padx = 29, pady = 20, command = button_divide)
button_equal = Button(root, text = "=", padx = 29, pady = 20, command = button_total)
button_clear = Button(root, text = "Clear", padx = 95, pady = 15, command = button_clear)

# These grid() calls place the operational buttons.
button_plus.grid(row = 4, column = 0)
button_minus.grid(row = 4, column = 2)
button_cross.grid(row = 5, column = 0)
button_by.grid(row = 5, column = 2)
button_equal.grid(row = 5, column = 1)
button_clear.grid(row = 6, column = 0, columnspan = 3)

root.mainloop()