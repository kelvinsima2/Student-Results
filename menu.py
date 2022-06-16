# This is the main program. Run the program to show a tkinter GUI menu.
# Select the function you would like to undertake, and click execute.
# Most of the diagrams will appear as pop up images, and
# the lists will appear in the python shell.
# This program was written by F134712, updated on the 17th of January 2022.

from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from testResults import display_result
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from studentPerformance import student_performance
from underperformingStudent import underperforming
from hardworkingStudents import hardworking




def execute():
    """ Displays a menu for the module leader to choose from. """
    text = click.get()
    if text == 'Access Student Test Results':
        label = Label(window, text = '''Please enter student ID
                      between 1 and 155''')
        label.pack()
        execute.txt = Entry(window, width = 10)
        execute.txt.pack()
        button1.pack()
        
        
      
    elif text == 'Relative and Absolute Student Performance':
        label1 = Label(window, text = '''Please enter student
        ID between 1 and 155''')
        label1.pack()
        execute.txt1 = Entry(window, width = 10)
        execute.txt1.pack()
        label2 = Label(window, text = 'Please select test')
        label2.pack()
        options2 = ['test1', 'test2', 'test3', 'test4', 'MockTest',
                    'SumTest']
        drop_down2 = OptionMenu(window, click_2, *options2)
        drop_down2.pack()
        button2.pack()
          

    elif text == 'Underperforming Students':
        label2 = Label(window, text = '''Click Enter to view the
        underperforming student list in the Python Shell''')
        label2.pack()
        button3.pack()

    else:
        if text == 'Hardworking Students':
            label3 = Label(window, text = '''Click Enter to view
            the hardworking student list in the Python Shell''')
            label3.pack()
            button4.pack()

def click1():
    """ Displays a student's results. """
    researchid = execute.txt.get()
    display_result(int(researchid))
    return

def click2():
    """ Displays a student's performance. """
    chosen_test = click_2.get()
    researchid = execute.txt1.get()
    student_performance(chosen_test, int(researchid))

def click3():
    """ Shows underperforming students."""
    underperforming()

def click4():
    """ Displays hardworking students. """
    hardworking()
    
window = Tk()

window.title('Student Monitoring System')
window.geometry('350x200')


options = [
    'Access Student Test Results',
    'Relative and Absolute Student Performance',
    'Underperforming Students',
    'Hardworking Students'
    ]
    

click = StringVar()
click_2 = StringVar()
click.set('Click here to Start')
click_2.set('Select Test')

drop_down = OptionMenu(window, click, *options)
drop_down.pack()

button = Button(window,  text = 'Execute', command = execute)
button.pack()

button1 = Button(window, text = "Enter", command = click1)
button2 = Button(window, text = "Enter", command = click2)
button3 = Button(window, text = "Enter", command = click3)
button4 = Button(window, text = "Enter", command = click4)

window.mainloop()
