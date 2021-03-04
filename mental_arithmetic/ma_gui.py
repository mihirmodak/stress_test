from tkinter import *
from mental_arithmetic import ma_variables  as db; 
from mental_arithmetic import ma_functions as fns;
# from mental_arithmetic import arithmetic_gui as ag

def main(root, s):
    db.init(root)
    fns.init(root)
    # # Set up the window
    # root = Tk()

    # from .resources import settings as s; s.init(root)
    # from mental_arithmetic import *

    root.title("Stress Test")
    root["padx"] = 100
    root["pady"] = 150 

    # Add timer
    db.label_t = Label(root, text='0.0',font=s.Heading) 
    db.label_t.grid(row= 0, column= 0,pady= 30)

    # Frame for Initial Setup (Checkboxes)
    checks = Frame(root)
    ## Add checkboxes
    db.checkbox = Checkbutton(checks, text="PASS", variable=db.var)
    db.checkbox.grid(row=1,column=3,padx=10,pady=10,sticky='W')

    db.checkbox1 = Checkbutton(checks, text="EASY", variable=db.var1)
    db.checkbox1.grid(row=1,column=0,padx=10,pady=10,sticky='W')

    db.checkbox2 = Checkbutton(checks, text="MODERATE", variable=db.var2)
    db.checkbox2.grid(row=1,column=1,padx=10,pady=10,sticky='W')

    db.checkbox3 = Checkbutton(checks, text="HARD", variable=db.var3)
    db.checkbox3.grid(row=1,column=2,padx=10,pady=10,sticky='W')

    db.checkbox4 = Checkbutton(checks, text="ADDITION", variable=db.var4)
    db.checkbox4.grid(row=2,column=0,padx=10,pady=10,sticky='W')

    db.checkbox5 = Checkbutton(checks, text="SUBTRACTION", variable=db.var5)
    db.checkbox5.grid(row=2,column=1,padx=10,pady=10,sticky='W')

    db.checkbox6 = Checkbutton(checks, text="MULTIPLICATION", variable=db.var6)
    db.checkbox6.grid(row=2,column=2,padx=10,pady=10,sticky='W')

    db.checkbox7 = Checkbutton(checks, text="DIVISION", variable=db.var7)
    db.checkbox7.grid(row=2,column=3,padx=10,pady=10,sticky='W')

    checks.grid(row=1)


    # Frame for instructions
    const_entry = Frame(root) # this frame will persist past the setup screen
    entryLabel = Label(const_entry, text="Answer:", font=s.Heading)
    entryLabel.grid(row=0,column=0,sticky='W')

    # Create an Entry Widget in textFrame
    db.entryWidget = Entry(const_entry, font = s.Heading)
    db.entryWidget.bind('<Return>', lambda event : fns.Submit(db.answer,db.entryWidget))
    db.entryWidget.grid(row =0,column=1,sticky='W')

    const_entry.grid(row=2, pady=30)

    # Directions 
    directions = ('Press Enter key to begin. Choose difficulty and test mode.')
    instructions = Label(root, text=directions, bg='orange')
    instructions.grid(row=3,column=0,pady=10)


    root.bind("<Return>", fns.start)
    root.focus_set()

    root.bind("<q>", fns.endProgram)


    # Run
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    from .. import settings as s
    main()