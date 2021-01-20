import os
import sys

from openpyxl import load_workbook
from tkinter import *
from tkinter import filedialog


# -----------------------------------
# Program Functions
# -----------------------------------

def choosefile():
    """User chooses a file for testing"""
    global file
    file = filedialog.askopenfilename(
        filetypes=[('log', '*.log'), ('txt', '*.txt')])
    log_file_var1.set(file)

def choosesave():
    """User decides where the output file will be saved"""
    global save
    save = filedialog.askdirectory()
    log_file_var2.set(save)

def transform():
    """This is the main function of the program.  It opens our input
    file, extracts the valuables and replaces them into an xlxs.
    """
    with open(file, "r") as quality:
        file1 = quality.readlines()
        files = iter(file1)
        for line in files:
            if tracker in line:
                # Found what we are looking for, now we process.
                get_serials(line)

    path = os.getcwd()
    template = load_workbook(
        path + "\\Templates\\barcode_template.xlsx")
    sheets = template.active

    num = 1
    for value in part_list:
        a = sheets['A'+ str(num)]
        a.value = value
        num += 1

    num = 1
    for value in serial_list:
        a = sheets['B'+ str(num)]
        a.value = value
        num += 1

    template.save(save + "\\Barcodes.xlsx")

def get_serials(p):
    """Adding part numbers and serial numbers to individual lists"""
    s = p.split()
    scrum = s.index('PID:')
    bum = s.index('SN:')
    part_list.append(s[scrum+ 1])
    serial_list.append("*"
                       + s[bum+ 1]
                       + "*")

def info():
    """Creates the Serial_to_Barcode info button"""
    toplevel = Toplevel(root, bg="gray95")
    toplevel.transient(root)
    toplevel.title("Program info")
    Label(
        toplevel, text="Serial to Barcodes", bg="gray95").pack(pady=20)
    Label(
        toplevel, text="This program extracts part and serial" + '\n'
                        "numbers from a quality file you choose" + '\n'
                        "into an .xlxs document with scannable barcodes."
                        + '\n', bg="gray95").pack(padx=20)
    Label(
        toplevel, text="Compatible filetypes: .log .txt" + '\n'
                        "Compatible devices: Cisco" + '\n', bg="gray95").pack(padx=20)
    Button(
        toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

def quit():
    """Quit button functionality, ends the current program"""
    sys.exit()

#-----------------------------------
#Serial to Barcodes
#-----------------------------------

part_list = []
serial_list = []
tracker = 'PID'
App_Version = "Serial_to_Barcodes v1.0"
root = Tk()
root.title(App_Version)
# Creating a canvas for placing modules
canvas_width = 380
canvas_height = 300
w = Canvas(
    root, width= canvas_width, height= canvas_height, bg='gray95')
w.pack()

# Modules the correspond to choosing the input file.
Label1 = Label(
    w, text="Quality file location:",font= "Helvetica 10 bold", bg='gray95')
Label1.place(x=20, y=25)
Btn0 = Button(
    w, text="Browse",command=choosefile, width=7)
Btn0.place(x=300, y=50)
log_file_var1 = StringVar()
log_file = Entry(
    w, width="45", textvariable=log_file_var1)
log_file.place(x=20, y=53)

# Modules that correspond to saving the output file.
Label2 = Label(
    w, text="Barcode output location:", font="Helvetica 10 bold", bg='gray95')
Label2.place(x=20, y=100)
Btn4 = Button(
    w, text="Browse", command=choosesave, width=7)
Btn4.place(x=300, y=125)
log_file_var2 = StringVar()
log_file = Entry(
    w, width="45", textvariable=log_file_var2)
log_file.place(x=20, y=128)

# Start, quit, and info buttons.
Btn1 = Button(
    w, text="Start", command=transform, width=13, height=1)
Btn1.place(x=20, y=250)
Btn2 = Button(
    w, text='Exit', command=quit, width=13, height=1)
Btn2.place(x=257, y=250)
Btn3 = Button(
    w, text="Info", command=info, width=13, height=1)
Btn3.place(x=138, y=250)

root.mainloop()