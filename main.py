from tkinter import *
from actions_for_calc import *


root = Tk()
root.title("Calculator")

input_number = Entry(root, width=49, borderwidth=3)
input_number.grid(column=0, row=0, columnspan=4)


# Create number buttons
button1 = Button(root, text='1', padx=30, pady=20, borderwidth=2, command=lambda: add_number('1', input_number))
button2 = Button(root, text='2', padx=30, pady=20, borderwidth=2, command=lambda: add_number('2', input_number))
button3 = Button(root, text='3', padx=30, pady=20, borderwidth=2, command=lambda: add_number('3', input_number))
button4 = Button(root, text='4', padx=30, pady=20, borderwidth=2, command=lambda: add_number('4', input_number))
button5 = Button(root, text='5', padx=30, pady=20, borderwidth=2, command=lambda: add_number('5', input_number))
button6 = Button(root, text='6', padx=30, pady=20, borderwidth=2, command=lambda: add_number('6', input_number))
button7 = Button(root, text='7', padx=30, pady=20, borderwidth=2, command=lambda: add_number('7', input_number))
button8 = Button(root, text='8', padx=30, pady=20, borderwidth=2, command=lambda: add_number('8', input_number))
button9 = Button(root, text='9', padx=30, pady=20, borderwidth=2, command=lambda: add_number('9', input_number))
button0 = Button(root, text='0', padx=67, pady=20, borderwidth=2, command=lambda: add_number('0', input_number))

# Create action buttons
button_add = Button(root, text='+', padx=30, pady=20, borderwidth=2, command=lambda: addition(input_number))
button_subtract = Button(root, text='-', padx=30, pady=20, borderwidth=2, command=lambda: subtract(input_number))
button_multiply = Button(root, text='*', padx=30, pady=20, borderwidth=2, command=lambda: multiply(input_number))
button_equal = Button(root, text='=', padx=67, pady=20, borderwidth=2, command=lambda: equal(input_number))

# Place buttons
button7.grid(column=0, row=1)
button8.grid(column=1, row=1)
button9.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)
button1.grid(column=0, row=3)
button2.grid(column=1, row=3)
button3.grid(column=2, row=3)
button_add.grid(column=3, row=1)
button_subtract.grid(column=3, row=2)
button_multiply.grid(column=3, row=3)
button0.grid(column=0, row=4, columnspan=2)
button_equal.grid(column=2, row=4, columnspan=2)

root.mainloop()
