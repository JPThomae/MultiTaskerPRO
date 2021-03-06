import subprocess

from tkinter import *

#======================================
#Package Imports Above
#======================================

def execute():
    """Pressing the start button when a program is selected
    will open a new shell to display the chosen program.
    """
    if variable.get() == 'Optic Tester':
        subprocess.call("Optic_TesterGUI.py", shell=True)
    elif variable.get() == 'Serial to Barcode':
        subprocess.call("Serial_to_BarcodeGUI.py", shell=True)

def info():
    """Creates the Serial_to_Barcode info button"""
    toplevel = Toplevel(root, bg="gray95")
    toplevel.transient(root)
    toplevel.title("Program info")
    Label(toplevel, text="MultiTaskerPRO", bg="gray95").pack(pady=20)
    Label(toplevel, text="This program serves as a tool" + '\n'
                        "selector which provides access" + '\n'
                        "to all available ThomaeCo. applications"
                        + '\n', bg="gray95").pack(padx=20)
    Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

def quit():
    """Quit button functionality, ends the current program"""
    import sys
    sys.exit()

# -----------------------------------
# MultitaskerPRO
# -----------------------------------

App_Version = 'Multitasker 1.0'
root = Tk()
root.title(App_Version)
# Adds a background image for style.
background = PhotoImage(
    file='Dependants/mtp_background.png')
w = background.width()
h = background.height()
canvas_width = w
canvas_height = h
# Creating a canvas for placing modules
m = Canvas(
    root, width=canvas_width, height=canvas_height, bg='gray95')
m.create_image(0, 0, image=background, anchor='nw')
m.pack()

# Menu for program selection.
programs = ['Serial to Barcode', 'Optic Tester']
variable = StringVar(root)
variable.set('Select a Program')
o = OptionMenu(m, variable, *programs)
o.config(width=18)
o.place(x=80, y=185)

# Start, quit and info buttons.
Btn10 = Button(
    m, text="Start", command=execute, width=9, height=1)
Btn10.place(x=40, y=350)
Btn20 = Button(
    m, text='Exit', command=quit, width=9, height=1)
Btn20.place(x=200, y=350)
Btn30 = Button(
    m, text="Info", command=info, width=9, height=1)
Btn30.place(x=115, y=80)

root.mainloop()


