from tkinter import *


root = Tk()
root.title("Calculator")

input = Entry(root, width = 35, borderwidth = 3)
input.grid(column=0, row=0, columnspan=3)

root.mainloop()