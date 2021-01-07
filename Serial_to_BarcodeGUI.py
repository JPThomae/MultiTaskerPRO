from openpyxl import load_workbook
import os
from tkinter import *
from tkinter import filedialog


#-----------------------------------
#Program Functions
#-----------------------------------

def ChooseFile():
    global file
    file = filedialog.askopenfilename(filetypes=[('log', '*.log'), ('txt', '*.txt')])
    log_file_var1.set(file)

def ChooseSave():
    global save
    save = filedialog.askdirectory()
    log_file_var2.set(save)

def Info():
    toplevel = Toplevel(root, bg="gray95")
    toplevel.transient(root)
    toplevel.title("Program info")
    Label(toplevel, text="Serial to Barcodes", bg="gray95").pack(pady=20)
    Label(toplevel, text="This program extracts part and serial" + '\n'
                        "numbers from a quality file you choose" + '\n'
                        "into an .xlxs document with scannable barcodes." + '\n', bg="gray95").pack(padx=20)
    Label(toplevel, text="Compatible filetypes: .log .txt" + '\n'
                        "Compatible devices: Cisco" + '\n', bg="gray95").pack(padx=20)
    Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

def Transform():
    with open(file, "r") as quality:
        file1 = quality.readlines()
        files = iter(file1)
        for line in files:
            if tracker in line:
                get_serials(line)

    path = os.getcwd()
    template = load_workbook(path + "\\Templates\\barcode_template.xlsx")
    sheets = template.active

    num = 1
    for value in part_list:
        a = sheets['A' + str(num)]
        a.value = value
        num += 1

    num = 1
    for value in serial_list:
        a = sheets['B' + str(num)]
        a.value = value
        num += 1

    template.save(save + "\\Barcodes.xlsx")

def get_serials(p):
    s = p.split()
    scrum = s.index('PID:')
    bum = s.index('SN:')
    part_list.append(s[scrum + 1])
    serial_list.append("*" + s[bum + 1] + "*")

def Quit():
    import sys;sys.exit()

#-----------------------------------
#Serial to Barcodes
#-----------------------------------

#Variable declarations
part_list = []
serial_list = []
tracker = 'PID'

App_Version = "Serial_to_Barcodes v1.0"
root = Tk()
root.title(App_Version)

canvas_width = 380
canvas_height = 300
w = Canvas(root, width=canvas_width, height=canvas_height, bg='gray95')
w.pack()

#Choosing the file
Label1 = Label(w, text="Quality file location:", font="Helvetica 10 bold", bg='gray95')
Label1.place(x=20, y=25)
Btn0 = Button(w, text="Browse", command=ChooseFile, width=7)
Btn0.place(x=300, y=50)
log_file_var1 = StringVar()
log_file = Entry(w, width="45", textvariable=log_file_var1)
log_file.place(x=20, y=53)

#Saving output
Label2 = Label(w, text="Barcode output location:", font="Helvetica 10 bold", bg='gray95')
Label2.place(x=20, y=100)
Btn4 = Button(w, text="Browse", command=ChooseSave, width=7)
Btn4.place(x=300, y=125)
log_file_var2 = StringVar()
log_file = Entry(w, width="45", textvariable=log_file_var2)
log_file.place(x=20, y=128)

#Start / End / Info program buttons
Btn1 = Button(w, text="Start", command=Transform, width=13, height=1)
Btn1.place(x=20, y=250)
Btn2 = Button(w, text='Exit', command=Quit, width=13, height=1)
Btn2.place(x=257, y=250)
Btn3 = Button(w, text="Info", command=Info, width=13, height=1)
Btn3.place(x=138, y=250)

root.mainloop()