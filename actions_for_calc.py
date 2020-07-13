from tkinter import *


def add_number(number, input_field):
    global number_in_field
    number_in_field += number
    input_field.delete(0, END)
    input_field.insert(0, number_in_field)


def addition(input_field):
    global number_in_memory
    global action_in_memory
    global number_in_field
    number_in_memory = int(input_field.get())
    action_in_memory = 'add'
    input_field.delete(0, END)
    number_in_field = ''


def subtract(input_field):
    global number_in_memory
    global action_in_memory
    global number_in_field
    number_in_memory = int(input_field.get())
    action_in_memory = 'subtract'
    input_field.delete(0, END)
    number_in_field = ''


def multiply(input_field):
    global number_in_memory
    global action_in_memory
    global number_in_field
    number_in_memory = int(input_field.get())
    action_in_memory = 'multiply'
    input_field.delete(0, END)
    number_in_field = ''


def equal(input_field):
    global number_in_memory
    global action_in_memory
    global number_in_field
    result = 0
    if action_in_memory == 'add':
        result = number_in_memory + int(number_in_field)
    if action_in_memory == 'subtract':
        result = number_in_memory - int(number_in_field)
    if action_in_memory == 'multiply':
        result = number_in_memory * int(number_in_field)
    input_field.delete(0, END)
    input_field.insert(0, str(result))
    number_in_memory = result
    number_in_field = ''
    action_in_memory = ''


number_in_field = ''
number_in_memory = 0
action_in_memory = ''
