# imports
from tkinter import *
from functools import partial
import variables as db; db.init()

import sys
sys.path.append('../')

# Set up the window
global root
root = Tk()
# make it look nice
root.title("Stress Test")
root["padx"] = 100
root["pady"] = 150 
db.root = root

# import custom functions
# import main_functions as fns; fns.init(root)


#import necessary tkinter settings and variables
import settings as s; s.init(db.root)

def main():

    # Create Frame to enter identifier
    iden = Frame(db.root)

    # Ask for identifier
    db.iden_label = Label(db.root, text="Enter the patient identifier", font=db.Heading)
    db.iden_label.grid(row=0, column=0, pady=30)

    # Create Text Entry Field 
    db.idenWidget = Entry(iden, font = s.Heading)
    # db.idenWidget.bind('<Return>', lambda: s.save_identifier(db.idenWidget))
    db.idenWidget.grid(row =1,column=0)

    iden.grid(row=1, pady=30)


    # Create Frame for starting selection menu
    tests = Frame(db.root)

    # Tests
    db.choice_label = Label(db.root, text='Choose a Test',font=db.Heading) 
    db.choice_label.grid(row= 2, column= 0,pady= 30)

    db.Button1 = Button(
        master= db.root, 
        text="Mental Arithmetic Test", 
        command= partial(s.activate_mental_arith, root, s, db.idenWidget),
        activebackground="blue", 
        activeforeground="white", 
        bg="white", 
        fg="black", 
        font=db.Heading,
        width = 50,
        state = NORMAL
        )
    db.Button1.grid(row=3, column=0, pady=10, sticky='W')

    db.Button2 = Button(
        master= db.root, 
        text="N-Back Test", 
        # command=partial(), 
        activebackground="blue", 
        activeforeground="white", 
        bg="white", 
        fg="black", 
        font=db.Heading,
        width = 50,
        state = DISABLED
        )
    db.Button2.grid(row=4, column=0, pady=10, sticky='W')

    db.Button3 = Button(
        master= db.root, 
        text="Stroop Color Test", 
        command=partial(s.activate_stroop, root, s, db.idenWidget), 
        activebackground="blue", 
        activeforeground="white", 
        bg="white", 
        fg="black", 
        font=db.Heading,
        width = 50,
        state = NORMAL
        )
    db.Button3.grid(row=5, column=0, pady=10, sticky='W')

    tests.grid(row = 2, pady=30)

    db.root.mainloop()

if __name__ == '__main__':
    main()