from tkinter import *
from tkinter import filedialog


#-----------------------------------
#Program Functions
#-----------------------------------

def DoTheThing():
    with open(file, "r") as quality:
        file1 = quality.readlines()
        files = iter(file1)
        for line in files:
            interfaces(line)
            wavelengths(line)
            loss(line)

    int_rx = [float(el) for el in rx]
    int_tx = [float(el) for el in tx]
    good_or_bad(interface, wavelength, int_tx, int_rx)

def ChooseFile():
    global file
    file = filedialog.askopenfilename(filetypes=[('log', '*.log'), ('txt', '*.txt')])
    log_file_var.set(file)

def interfaces(line):
    for i in target:
        if i in line:
            s = line.strip()
            n = s[-15:]
            if n[-3] == '/' and ('T' + n) not in interface:
                interface.append('T' + n)
            elif n[-2] == '/' and n not in interface:
                interface.append(n)

def wavelengths(line):
    if 'Media type: R fiber over' in line:
        wavelength.append(line[-14:-10].strip())

def loss(line):
    if '0     n/a' in line:
        if len(tx) < len(interface):
            p = line.strip()
            tx.append(p[14:18].strip())
        if len(rx) < len(interface):
            rx.append(p[32:37].strip())

def good_or_bad(interface, wavelength, tx, rx):
    for i in range(0, len(interface)):
        diff = rx[i] - tx[i]
        if wavelength[i] == '1310':
            if rx[i] == 0 and tx[i] == 0:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- No Signal' + '\n')
            elif rx[i] < -30 or tx[i] < -30:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- No Signal' + '\n')
            elif diff > -13:
                textbox.insert(END, interface[i] + ': ' + 'PASS --- ' + str(round(diff, 3)) + '\n')
            elif diff < -13:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- ' + str(round(diff, 3)) + '\n')
        if wavelength[i] == '850':
            if rx[i] == 0 and tx[i] == 0:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- No Signal' + '\n')
            elif rx[i] < -30 or tx[i] < -30:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- No Signal' + '\n')
            elif diff > -3:
                textbox.insert(END, interface[i] + ': ' + 'PASS --- ' + str(round(diff, 3)) + '\n')
            elif diff < -3:
                textbox.insert(END, interface[i] + ': ' + 'FAIL --- ' + str(round(diff, 3)) + '\n')

def Info():
    toplevel = Toplevel(root, bg="gray95")
    toplevel.transient(root)
    toplevel.title("Program info")
    Label(toplevel, text="4206 Optic Loss Tester", bg="gray95").pack(pady=20)
    Label(toplevel, text="To use: Browse to the" + '\n'
                         "quality file you wish to test" + '\n'
                         "and click Start Test.", bg="gray95").pack()
    Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

def quit():
    import sys;sys.exit()

#-----------------------------------
#Optic Tester
#-----------------------------------

#Variable declarations
interface = []
wavelength = []
tx = []
rx = []
target = ['#show controller  TenGigE 0/0/0/']

App_Version = "Optic Tester v1.0"
root = Tk()
root.title(App_Version)

canvas_width = 380
canvas_height = 500
w = Canvas(root, width=canvas_width, height=canvas_height, bg='gray95')
w.pack()

textbox = Text(w, height=17, width=42)
textbox.place(x=20, y=150)

#Choosing the file
Label1 = Label(w, text="Quality log file location:", font="Helvetica 10 bold", bg='gray95')
Label1.place(x=20, y=25)
Btn0 = Button(w, text="Browse", command=ChooseFile, width=7)
Btn0.place(x=300, y=50)
log_file_var = StringVar()
log_file = Entry(w, width="45", textvariable=log_file_var)
log_file.place(x=20, y=53)

#Start / End / Info program buttons
Btn1 = Button(w, text="Start Test", command=DoTheThing, width=15, height=1)
Btn1.place(x=20, y=95)
Btn2 = Button(w, text='Exit', command=quit, width=15, height=1)
Btn2.place(x=130, y=450)
Btn3 = Button(w, text="Info", command=Info, width=15, height=1)
Btn3.place(x=244, y=95)

root.mainloop()



