import tkinter as tk
from decimal import Decimal

number = 0
calculations = [] #will be populated by a pattern of numbers and mathematical operators.
finished = False #will be true once the user hits the equal sign, so that further input will reset the display.

"""
The following 4 functions get the number on screen and add it to calculations, followed by the mathematical operation
to be performed.
"""

def add():
    calculations.append(getNum())
    calculations.append("+")
    clear()

def subtract():
    calculations.append(getNum())
    calculations.append("-")
    clear()

def multiply():
    calculations.append(getNum())
    calculations.append("*")
    clear()

def divide():
    calculations.append(getNum())
    calculations.append("/")
    clear()

def equals(): #runs through the calculation list, performing mathematical operations in the order they were inputted.
    global finished #Unsure why, but weird bugs or runtime errors pop up if finished is not made global.
    calculations.append(getNum())
    for i in range(0, len(calculations), 2): #By only looking at even-numbered indices (where the numbers are), I thought I could reduce runtime complexity as practice for writing more efficient code.
        if i == 0:
            number = float(calculations[i]) #Making sure the first number in the array is included in the calculation.
        else:
            if calculations[i-1] == "+":
                number += float(calculations[i])
            elif calculations[i-1] == "-":
                number -= float(calculations[i])
            elif calculations[i-1] == "*":
                number *= float(calculations[i])
            elif calculations[i-1] == "/":
                try: #try-except block for if user tries to divide by zero.
                    number /= float(calculations[i])
                except ZeroDivisionError:
                    number = 0
                    calculations.clear()
                    error_window = tk.Tk()
                    error_label = tk.Label(error_window, text="Error: Division by zero")
                    error_label.grid(row=0, column=0)
                    return
    display["text"] = Decimal(str(number).rstrip("0")) #using this to get rid of trailing zeroes
    finished = True
    calculations.clear()
    number = 0
        
def getNum():
    return float(display["text"])

def hasDecimal(): #checks if the number inputted has a decimal point.
    for i in display["text"]:
        if i == ".":
            return True
    return False

def display_input(x):
    global finished #Unsure why, but weird bugs or runtime errors pop up if finished is not made global.
    if (display["text"] == "0" and x != "."): #By default the display is reset before the user input is displayed, unless the number to be inputted is a decimal.
        display["text"] = ""
        display["text"] += x
    elif finished == True: #Resets the display before displaying user input if a calculation has been finished.
        display["text"] = ""
        display["text"] += x
        finished = False
    else:
        if x == "." and not(hasDecimal()): #this is to prevent the user from inputting multiple decimal points into one number.
            print("test")
            display["text"] += x
        elif x != ".":
            display["text"] += x

def clear():
    display["text"] = "0"
    number = 0

window = tk.Tk()
window.title("Calculator")
top_frame = tk.Frame(window, width=300, height=50, pady=5)
bottom_frame = tk.Frame(window, width=300, height=250, pady=5)
top_frame.grid(row=0, column=0)
bottom_frame.grid(row=1, column=0)
display = tk.Label(top_frame, text="0")
display.grid(row=0, column=0)
button_1 = tk.Button(bottom_frame, text = "1", height=2, width=3, command=lambda:display_input("1"))
button_2 = tk.Button(bottom_frame, text = "2", height=2, width=3, command=lambda:display_input("2"))
button_3 = tk.Button(bottom_frame, text = "3", height=2, width=3, command=lambda:display_input("3"))
button_4 = tk.Button(bottom_frame, text = "4", height=2, width=3, command=lambda:display_input("4"))
button_5 = tk.Button(bottom_frame, text = "5", height=2, width=3, command=lambda:display_input("5"))
button_6 = tk.Button(bottom_frame, text = "6", height=2, width=3, command=lambda:display_input("6"))
button_7 = tk.Button(bottom_frame, text = "7", height=2, width=3, command=lambda:display_input("7"))
button_8 = tk.Button(bottom_frame, text = "8", height=2, width=3, command=lambda:display_input("8"))
button_9 = tk.Button(bottom_frame, text = "9", height=2, width=3, command=lambda:display_input("9"))
button_0 = tk.Button(bottom_frame, text = "0", height=2, width=3, command=lambda:display_input("0"))
button_decimal = tk.Button(bottom_frame, text = ".", height=2, width=3, command=lambda:display_input("."))
button_add = tk.Button(bottom_frame, text = "+", height=2, width=3, command=lambda:add())
button_subtract = tk.Button(bottom_frame, text = "-", height=2, width=3, command=lambda:subtract())
button_multiply = tk.Button(bottom_frame, text = "X", height=2, width=3, command=lambda:multiply())
button_divide = tk.Button(bottom_frame, text = "/", height=2, width=3, command=lambda:divide())
button_equals = tk.Button(bottom_frame, text="=", height=2, width=3, command=lambda:equals())
button_clear = tk.Button(bottom_frame, text="C", height=2, width=3, command=lambda:clear())
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=3, column=0)
button_decimal.grid(row=3, column=1)
button_add.grid(row=0, column =3)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_equals.grid(row=3, column=2)
button_clear.grid(row=0, column=4)
window.mainloop()