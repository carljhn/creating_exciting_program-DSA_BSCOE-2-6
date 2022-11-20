#              Seatwork
# - Create a program of your choice.
# - You may get inspiration from YouTube.com
# - Your should include the purpose/idea of the program and where can it be applied.
# - Upload the demo in Messenger before 4pm
# - Include the link / reference of your program in README or comment in the code

#import tkinter
from tkinter import *

#define a function for text display
def TimeTable():
    for x in range(1, 15):
        m = int(textInput.get())
        textDisplay.insert(END, (x), '\t', " x ", '\t', (m), '\t', " = ", '\t', (x * m))
        textDisplay.insert(END, '\n\n')

#========CONTAINER=========#
Multiply = Tk ()
Multiply.title("Times Table")
Multiply.resizable (0, 0)
textInput = StringVar()

#========WIDGET 1=========#
label = Label(Multiply, text = "Multiplication Table", font = ("arial", 20, "bold"), 
        fg = "black").grid(row = 0, column = 0)

#========WIDGET 2=========#
txtInput = Entry(Multiply, textvariable = textInput, bd = 30, font = ("arial", 20, "bold"), 
            insertwidth = 4, bg = "powder blue", justify = "center").grid(row = 1, column = 0)

#========WIDGET 3=========#
textDisplay = Text(Multiply, width = 30, height = 23, bg = "powder blue", bd =  16, font = ("arial", 10, "bold"))
textDisplay.grid(row = 2, column = 0)

#========BUTTON=========#
buttonTimesTable = Button(Multiply, padx = 16, pady = 16, bd = 8, fg = "black", font = ("arial", 20, "bold"), 
                    text="Show Times Table", bg = "powder blue", command = TimeTable, width = 18).grid(row = 3, column = 0)

Multiply.mainloop()

#========Application====#
#   This python program, which is about Time Tables, would be helpful 
#   especially for younger users who are building a strong foundation on
#   multiplication of integers. This can be used to help them in mock exams or 
#   math practices.

#========Reference====#
#   https://www.youtube.com/watch?v=58HbLHpTBuw
#   Credits to: DJ Oamen