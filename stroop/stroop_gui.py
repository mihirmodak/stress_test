from tkinter import *
from stroop import stroop_variables as db
from stroop import stroop_functions as fns
# from functools import partial


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
    initial = Frame(root)
    db.checkbox1 = Checkbutton(initial, text="EASY", variable=db.diffic_easy)
    db.checkbox1.grid(row=1,column=0,padx=10,pady=10,sticky='W')

    db.checkbox2 = Checkbutton(initial, text="MODERATE", variable=db.diffic_med)
    db.checkbox2.grid(row=1,column=1,padx=10,pady=10,sticky='W')

    db.checkbox3 = Checkbutton(initial, text="HARD", variable=db.diffic_hard)
    db.checkbox3.grid(row=1,column=2,padx=10,pady=10,sticky='W')

    db.start_button = Button(
        master= db.root, 
        text="Begin", 
        command= fns.start,
        activebackground="blue", 
        activeforeground="white", 
        bg="white", 
        fg="black", 
        font=s.Heading,
        width = 50,
        state = NORMAL
    )
    db.start_button.grid(row=2, column=0, pady=10, sticky='W')

    initial.grid(row=1)


    root.bind(db.start_button, fns.start)
    root.focus_set()

    root.bind("<q>", fns.endProgram)


    # Run
    root.mainloop()
