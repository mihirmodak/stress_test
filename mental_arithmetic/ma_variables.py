from tkinter import *

# Fix Identifier Not Found Error
import variables as master_db; master_db.init()
global identifier
identifier= master_db.identifier

def init(ma_root):
    # Timer & Checkbox
    global label
    global var
    var = IntVar()

    global var1
    var1 = IntVar()

    global var2
    var2 = IntVar()

    global var3
    var3 = IntVar()

    global var4
    var4 = IntVar()

    global var5
    var5 = IntVar()

    global var6
    var6 = IntVar()
    
    global var7
    var7 = IntVar()

    global checkbox
    checkbox = Checkbutton()

    global checkbox1
    checkbox1 = Checkbutton()

    global checkbox2
    checkbox2 = Checkbutton()

    global checkbox3
    checkbox3 = Checkbutton()

    global checkbox4
    checkbox4 = Checkbutton()

    global checkbox5
    checkbox5 = Checkbutton()

    global checkbox6
    checkbox6 = Checkbutton()

    global checkbox7
    checkbox7 = Checkbutton()

    # create_record
    global filename
    filename = ""

    # Questions
    global trials
    global label1
    global num_range1
    global num_range2
    global mode

    # Start
    global label_t
    label_t = Label()
    global answer
    global timer
    global default_time
    global file

    # Submit
    global label2

    # Main
    global entryWidget
    entryWidget = Entry()

    global instructions
    instructions = Label()
    
    global identifier
    global root
    root = ma_root