from tkinter import *
import time
# import tkMessageBox
import tkinter.messagebox
import random
from datetime import datetime
import sys, os

# Timer & Checkbox
global label
global var
global var1
global var2
global var3

global var4
global var5
global var6
global var7

global checkbox
global checkbox1
global checkbox2
global checkbox3

global checkbox4
global checkbox5
global checkbox6
global checkbox7

def create_record():

    if sys.platform == "linux":
        if os.path.isdir(f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}"):
            save_folder = str(os.getcwd()) + f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}"
        else:
            os.makedirs(f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}")
            save_folder = str(os.getcwd()) + f"./saves/{str(datetime.now().strftime('%Y-%m-%d'))}"

    elif sys.platform == "win32":
        if os.path.isdir(f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"):
            save_folder = str(os.getcwd()) + f"\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"
        else:
            os.makedirs(f".\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\")
            save_folder = str(os.getcwd()) + f"\\saves\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"

    # filename = save_folder + str(datetime.now().strftime("%H-%M-%S") +f'-{identifier}.txt')
    filename = str(save_folder + str(datetime.now().strftime("%H-%M-%S") +'.txt'))

    file = open(filename,"w+")

    return file

def Questions():    

    global trials
    global label1
    global num_range1
    global num_range2
    global mode


    number1 = random.randrange(num_range1[0],num_range1[1])
    number2 = random.randrange(num_range2[0],num_range2[1])

    a = random.choice(mode)

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


    if trials == 0:
        label1 = Label(root, text=prompt, width=45, bg='yellow',font=("Helvetica", 30, 'bold'))
        label1.grid(row =3,pady=20)
    else:
        label1 = Label(root)
        label1.config(text = prompt)

    return answer

def start(event):
    global label_t
    global answer
    global trials
    global timer
    global default_time

    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global num_range1
    global num_range2
    global mode
    global file

    file = create_record()

    mode = []
    mode1 = []


    if var1.get() == 1:
        num_range1 = [1,10]
        num_range2 = [1,10]
        difficulty = "EASY"

    elif var2.get() == 1:
        num_range1 = [11,50]
        num_range2 = [1,10]
        difficulty = "MODERATE"

    elif var3.get() == 1:
        num_range1 = [11,100]
        num_range2 = [11,100]
        difficulty = "HARD"
    else:
        instructions.config(text="Please select difficulty")
        return


    if var4.get() == 1:
        mode.append(1)
        mode1.append("ADDITION")
    if var5.get() == 1:
        mode.append(2)
        mode1.append("SUBTRACTION")
    if var6.get() == 1:
        mode.append(3)
        mode1.append("MULTIPLICATION")
    if var7.get() == 1:
        mode.append(4)
        mode1.append("DIVISION")


    instructions.destroy()
    checkbox.destroy()
    checkbox1.destroy()
    checkbox2.destroy()
    checkbox3.destroy()
    checkbox4.destroy()
    checkbox5.destroy()
    checkbox6.destroy()
    checkbox7.destroy()
    entryWidget.focus_set()


    trials = 0
    answer = Questions()
    default_time = time.time()
    start_time = round(time.time()-default_time,2)
    timer = start_time



    file.write(difficulty+' ' + str(mode1) + '\n')

    print(difficulty, mode1[0:])

    file.write("START,     Time Stamp: {}\n".format(start_time))
    print("START,      Time Stamp: ", start_time)

    while True:
        # put the timer value into the label
        label_t.config(text=str(timer))
        # wait for 0.1 seconds
        time.sleep(0.1)
        # needed with time.sleep()
        root.update()
        # update timer
        timer = round(time.time() - default_time,2)


def moveon():

    global answer
    global trials

    answer = Questions()

def endProgram(event):
    global file

    file.close()
    root.destroy()



def Submit(answer, entryWidget):
    """ Display the Entry text value. """

    global trials
    global label2
    global var

    trials += 1
    width_label = len("Please enter a number.")

    try:
        temp = int(entryWidget.get().strip())
    except ValueError:
        message = ("Type integers")
        if trials == 1:
            label2 = Label(root, text=message, width=width_label, font=("Helvetica", 20))
            label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            label2 = Label(root)
            label2.config(text = message)
            entryWidget.delete(0, 'end')

    if entryWidget.get().strip() == "":
        message = ("Please enter a number.")
        if trials == 1:
            label2 = Label(root, text=message, width=width_label, font=("Helvetica", 20))
            label2.grid(row=4)
            entryWidget.delete(0, 'end')
            
        else:
            label2.config(text = message)
            entryWidget.delete(0, 'end')
            
      
    elif answer != int(entryWidget.get().strip()):
        message = ("Wrong")
        if trials == 1:
            label2 = Label(root, text= message, width=width_label, fg='red', font=("Helvetica", 20))
            label2.grid(row=4)
            entryWidget.delete(0, 'end')

        else:
            label2.config(text = message)
            entryWidget.delete(0, 'end')

        if var.get() == 1:
            file.write("Wrong,      Time Stamp: {}\n".format(round(time.time()-default_time,2)))
            print("Wrong,      Time Stamp: ", round(time.time()-default_time,2))
            moveon()
            
    else:
        message = ("Correct")
        if trials == 1:
            label2 = Label(root, text= message, width=width_label, font=("Helvetica", 20))
            label2.grid(row=4)
            entryWidget.delete(0, 'end')
        else:
            label2.config(text = message)
            entryWidget.delete(0, 'end')

        file.write("Correct,   Time Stamp: {}\n".format(round(time.time()-default_time,2)))
        print("Correct,    Time Stamp: ", round(time.time()-default_time,2))
        moveon()


if __name__ == "__main__":      

    # create a Tkinter window
    root = Tk()

    root.title("Mental Arithmetic")
    root["padx"] = 100
    root["pady"] = 150  

    label_t = Label(root, text='0.0',font=("Helvetica", 30),width= 20) 
    label_t.grid(row = 0, column =0,pady=30)

    var = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()

    frame1 = Frame(root)

    checkbox = Checkbutton(frame1, text="PASS", variable=var,font=("Helvetica", 20))
    checkbox.grid(row=1,column=3,padx=10,pady=10,sticky='W')

    checkbox1 = Checkbutton(frame1, text="EASY", variable=var1,font=("Helvetica", 20))
    checkbox1.grid(row=1,column=0,padx=10,pady=10,sticky='W')

    checkbox2 = Checkbutton(frame1, text="MODERATE", variable=var2,font=("Helvetica", 20))
    checkbox2.grid(row=1,column=1,padx=10,pady=10,sticky='W')

    checkbox3 = Checkbutton(frame1, text="HARD", variable=var3,font=("Helvetica", 20))
    checkbox3.grid(row=1,column=2,padx=10,pady=10,sticky='W')

    checkbox4 = Checkbutton(frame1, text="ADDITION", variable=var4,font=("Helvetica", 20))
    checkbox4.grid(row=2,column=0,padx=10,pady=10,sticky='W')

    checkbox5 = Checkbutton(frame1, text="SUBSTRACTION", variable=var5,font=("Helvetica", 20))
    checkbox5.grid(row=2,column=1,padx=10,pady=10,sticky='W')

    checkbox6 = Checkbutton(frame1, text="MULTIPLICATION", variable=var6,font=("Helvetica", 20))
    checkbox6.grid(row=2,column=2,padx=10,pady=10,sticky='W')

    checkbox7 = Checkbutton(frame1, text="DIVISION", variable=var7,font=("Helvetica", 20))
    checkbox7.grid(row=2,column=3,padx=10,pady=10,sticky='W')

    frame1.grid(row=1)


    # Create frame for instruction and button
    frame2 = Frame(root)

    # Create a Label in textFrame
    entryLabel = Label(frame2,font=("Helvetica", 30),width=10)
    entryLabel["text"] = "Answer:"
    entryLabel.grid(row=0,column=0,sticky='W')


    # Create an Entry Widget in textFrame
    global entryWidget
    entryWidget = Entry(frame2, font = ("Helvetica", 30), width= 30)
    entryWidget.bind('<Return>', lambda event : Submit(answer,entryWidget))
    entryWidget.grid(row =0,column=1,sticky='W')


    frame2.grid(row=2,pady=30)


    # Directions 
    global instructions     
    directions = ('Press Enter key to begin. Choose difficulty and test mode.')
    instructions = Label(root, text=directions, width=len(directions), bg='orange',font=("Helvetica", 20))
    instructions.grid(row=3,column=0,pady=10)


    root.bind("<Return>", start)
    root.focus_set()

    root.bind("<q>", endProgram)


    # start the event loop
    root.mainloop()
