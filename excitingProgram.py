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