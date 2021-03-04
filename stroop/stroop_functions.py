from tkinter import *
import random
import time


import variables as master_db; master_db.init()
import settings as s
global identifier
identifier= master_db.identifier

from stroop import stroop_variables as db

def init(stroop_root):
    global root
    root = stroop_root
    db.init(stroop_root)
    s.init(stroop_root)

def Questions():

    color = random.choice(db.options)
    word = random.choice(db.options).upper()
    

    codes = {'green':'g', 'blue':'b', 'yellow':'y', 'red':'r'}

    answer = codes[color]

    # if db.trials == 0:
    db.label1 = Label(root, text=word, width=45, bg='gray', fg=color, font=master_db.Heading)
    db.label1.grid(row =3,pady=20)
    # else:
    #     db.label1 = Label(root)
    #     db.label1.config(text = word, fg=color)

    return answer

def endProgram():
    # global file

    # db.file.close()
    db.root.destroy()
    master_db.root.mainloop()

def Submit(answer, entryWidget):

    if entryWidget.get().strip() == "q":
        endProgram()

    db.trials += 1
    width_label = len("Please enter one of the following characters: r, g, y, b, q.")

    try:
        temp = entryWidget.get().strip()
    except ValueError:
        message = ("Type color code")
        if db.trials == 1:
            db.label2 = Label(root, text=message, width=width_label, font=master_db.Heading)
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            db.label2 = Label(root)
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

    if entryWidget.get().strip() == "":
        message = ("Unable to process input")
        if db.trials == 1:
            db.label2 = Label(root, text=message, width=width_label, font=master_db.Heading)
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
            
        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')
            
      
    elif answer != entryWidget.get().strip():
        message = ("Wrong")
        if db.trials == 1:
            db.label2 = Label(root, text= message, width=width_label, fg='red', font=master_db.Heading)
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')

        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

        # if db.var == 1:
        # db.file.write("Wrong,      Time Stamp: {}\n\n".format(round(time.time()-db.default_time,2)))
        print("Wrong,      Time Stamp: ", round(time.time()-db.default_time,2))
        moveon()
            
    else:
        message = ("Correct")
        if db.trials == 1:
            db.label2 = Label(root, text= message, width=width_label, font=master_db.Heading)
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

        # db.file.write("Correct,   Time Stamp: {}\n\n".format(round(time.time()-db.default_time,2)))
        print("Correct,    Time Stamp: ", round(time.time()-db.default_time,2))
        moveon()

def moveon():
    db.answer = Questions()

def start():
    # db.init(root)
    # global label_t
    # global answer
    # global trials
    # global timer
    # global default_time

    # global var1
    # global var2
    # global var3
    # global var4
    # global var5
    # global var6
    # global var7
    # global num_range1
    # global num_range2
    # global mode
    # global file

    # if not os.path.isfile(db.filename):
    #     create_record()

    db.mode = []
    db.mode1 = []


    if db.diffic_easy.get() == 1:
        db.congruent_prop = 0.75
        difficulty = "EASY"

    elif db.diffic_med.get() == 1:
        db.congruent_prop = 0.5
        difficulty = "MODERATE"

    elif db.diffic_hard.get() == 1:
        db.congruent_prop = 0.25
        difficulty = "HARD"
    else:
        db.instructions.config(text="Please select difficulty")
        return

    db.instructions.destroy()
    db.start_button.destroy()
    db.checkbox1.destroy()
    db.checkbox2.destroy()
    db.checkbox3.destroy()
    db.entryWidget.focus_set()

    # Frame for instructions
    const_entry = Frame(root) 
    entryLabel = Label(const_entry, text="Answer:", font=s.Heading)
    entryLabel.grid(row=0,column=0,sticky='W')

    # Create an Entry Widget in textFrame
    db.entryWidget = Entry(const_entry, font = s.Heading)
    db.entryWidget.bind('<Return>', lambda event : Submit(db.answer,db.entryWidget))
    db.entryWidget.grid(row=0,column=1,sticky='W')

    const_entry.grid(row=1, pady=30)


    db.trials = 0
    db.answer = Questions()
    db.default_time = time.time()
    start_time = round(time.time()-db.default_time,2)
    db.timer = start_time

    # db.file.write(difficulty+' ' + str(db.mode1) + '\n')

    print(difficulty, db.mode1[0:])

    # db.file.write("START,     Time Stamp: {}\n".format(start_time))
    print("START,      Time Stamp: ", start_time)

    while True:
        # put the timer value into the label
        db.label_t.config(text=str(db.timer))
        # wait for 0.1 seconds
        time.sleep(0.1)
        # needed with time.sleep()
        root.update()
        # update timer
        db.timer = round(time.time() - db.default_time,2)
