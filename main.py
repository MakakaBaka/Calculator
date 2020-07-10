from tkinter import *


class MyButton:
    def __init__(self, meaning, width, height, position_x, position_y, action):
        self.meaning = meaning
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.action = action

    def place_button(self):
        self = Button(root, text=self.meaning, padx=self.width, pady=self.height, command=self.action)
        print(self.position_x)
        self.grid(row=self.position_x, column=self.position_y)

def passing():
    pass

root = Tk()
root.title("Calculator")

zero = MyButton('0', 40, 20, 0, 0, passing)
zero.place_button()
zero = MyButton('1', 40, 20, 0, 0, passing)
zero.place_button()
zero = MyButton('2', 40, 20, 0, 0, passing)
zero.place_button()

root.mainloop()