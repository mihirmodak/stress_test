import random
from datetime import datetime
import sys, os
import subprocess
from tkinter import *
from mental_arithmetic import ma_variables  as db; 

# Fix Identifier Not Found Error
import variables as master_db; master_db.init()

import time

def init(ma_root):
    global root
    root = ma_root
    db.init(ma_root)

def sr_setup():
    # implement pip as a subprocess
    if sys.platform == "linux":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

    if sys.platform == "win32":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyAudio-0.2.11-cp39-cp39-win_amd64.whl'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speechrecognition~=3.8.1'])
    
    import speech_recognition as sr

def create_record():

    if sys.platform == "linux":
        if os.path.isdir(f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}/{master_db.identifier}"):
            save_folder = str(os.getcwd()) + f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}/{master_db.identifier}"
        else:
            os.makedirs(f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}/{master_db.identifier}")
            save_folder = str(os.getcwd()) + f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}/{master_db.identifier}"

    if sys.platform == "win32":
        if os.path.isdir(f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\{master_db.identifier}\\"):
            save_folder = str(os.getcwd()) + f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\{master_db.identifier}\\"
        else:
            os.makedirs(f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\{master_db.identifier}\\")
            save_folder = str(os.getcwd()) + f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\{master_db.identifier}\\"

    # filename = save_folder + str(datetime.now().strftime("%H-%M-%S") +f'-{identifier}.txt')
    db.filename = str(save_folder) + "mental_arithmetic.txt"

    db.file = open(db.filename,"a+")

def Questions():    

    # global trials
    # global label1
    # global num_range1
    # global num_range2
    # global mode


    number1 = random.randrange(db.num_range1[0],db.num_range1[1])
    number2 = random.randrange(db.num_range2[0],db.num_range2[1])

    a = random.choice(db.mode)

    if a == 1:
        answer = number1 + number2
        prompt = (str(number1) + " + " + str(number2))
    elif a == 2:
        answer = max(number1,number2) - min(number1,number2)
        prompt = (str(max(number1,number2)) + " - " + str(min(number1,number2)))
    elif a == 3:
        answer = number1 * number2
        prompt = (str(number1) + " * " + str(number2))
    elif a == 4:
        temp_answer = number1 * number2
        answer = number1
        prompt = (str(temp_answer) + " / " + str(number2))


    if db.trials == 0:
        db.label1 = Label(root, text=prompt, width=45, bg='yellow',font=("Helvetica", 30, 'bold'))
        db.label1.grid(row =3,pady=20)
    else:
        db.label1 = Label(root)
        db.label1.config(text = prompt)

    return answer

def start(event):
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

    if not os.path.isfile(db.filename):
        create_record()

    db.mode = []
    db.mode1 = []


    if db.var1.get() == 1:
        db.num_range1 = [1,10]
        db.num_range2 = [1,10]
        difficulty = "EASY"

    elif db.var2.get() == 1:
        db.num_range1 = [11,50]
        db.num_range2 = [1,10]
        difficulty = "MODERATE"

    elif db.var3.get() == 1:
        db.num_range1 = [11,100]
        db.num_range2 = [11,100]
        difficulty = "HARD"
    else:
        db.instructions.config(text="Please select difficulty")
        return


    if db.var4.get() == 1:
        db.mode.append(1)
        db.mode1.append("ADDITION")
    if db.var5.get() == 1:
        db.mode.append(2)
        db.mode1.append("SUBTRACTION")
    if db.var6.get() == 1:
        db.mode.append(3)
        db.mode1.append("MULTIPLICATION")
    if db.var7.get() == 1:
        db.mode.append(4)
        db.mode1.append("DIVISION")


    db.instructions.destroy()
    db.checkbox.destroy()
    db.checkbox1.destroy()
    db.checkbox2.destroy()
    db.checkbox3.destroy()
    db.checkbox4.destroy()
    db.checkbox5.destroy()
    db.checkbox6.destroy()
    db.checkbox7.destroy()
    db.entryWidget.focus_set()


    db.trials = 0
    db.answer = Questions()
    db.default_time = time.time()
    start_time = round(time.time()-db.default_time,2)
    db.timer = start_time



    db.file.write(difficulty+' ' + str(db.mode1) + '\n')

    print(difficulty, db.mode1[0:])

    db.file.write("START,     Time Stamp: {}\n".format(start_time))
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

def moveon():

    # global answer
    # global trials

    db.answer = Questions()

def endProgram(event):
    # global file

    db.file.close()
    db.root.destroy()
    master_db.root.mainloop()

def Submit(answer, entryWidget):
    """ Display the Entry text value. """

    # global trials
    # global label2
    # global var

    db.trials += 1
    width_label = len("Please enter a number.")

    try:
        temp = int(entryWidget.get().strip())
    except ValueError:
        message = ("Type integers")
        if db.trials == 1:
            db.label2 = Label(root, text=message, width=width_label, font=("Helvetica", 20))
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            db.label2 = Label(root)
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

    if entryWidget.get().strip() == "":
        message = ("Please enter a number.")
        if db.trials == 1:
            db.label2 = Label(root, text=message, width=width_label, font=("Helvetica", 20))
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
            
        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')
            
      
    elif answer != int(entryWidget.get().strip()):
        message = ("Wrong")
        if db.trials == 1:
            db.label2 = Label(root, text= message, width=width_label, fg='red', font=("Helvetica", 20))
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')

        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

        # if db.var == 1:
        db.file.write("Wrong,      Time Stamp: {}\n\n".format(round(time.time()-db.default_time,2)))
        print("Wrong,      Time Stamp: ", round(time.time()-db.default_time,2))
        moveon()
            
    else:
        message = ("Correct")
        if db.trials == 1:
            db.label2 = Label(root, text= message, width=width_label, font=("Helvetica", 20))
            db.label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            db.label2.config(text = message)
            entryWidget.delete(0, 'end')

        db.file.write("Correct,   Time Stamp: {}\n\n".format(round(time.time()-db.default_time,2)))
        print("Correct,    Time Stamp: ", round(time.time()-db.default_time,2))
        moveon()

