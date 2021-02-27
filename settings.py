from tkinter import *
from tkinter.font import Font, nametofont
import variables as db; db.init()
from mental_arithmetic import ma_gui
import os
from datetime import datetime

def init(tk_root):
    db.root = tk_root

    global identifier
    identifier = None
    db.identifier = identifier

    # add more settings/functionality if needed
    fonts()

# Define Fonts
def fonts(): 
    nametofont('TkDefaultFont').config(family="Helvetica", size=20)
    
    global Heading
    Heading = Font(
        family="Helvetica", 
        size = 30,
        weight="bold"
    )
    db.Heading = Heading

def activate_mental_arith(root, s, entryWidget):
    db.iden_label.destroy()
    # db.idenWidget.destroy()
    db.choice_label.destroy()
    db.Button1.destroy()
    db.Button2.destroy()
    db.Button3.destroy()
    save_identifier(entryWidget)
    ma_gui.main(root, s)

def save_identifier(entryWidget):
    db.identifier = entryWidget.get().strip()
    print(db.identifier)

def log(e):
    if sys.platform == "linux":
        if os.path.isdir(f"./logs/{str(datetime.now().strftime('%Y-%m-%d'))}"):
            save_folder = str(os.getcwd()) + f"./logs/{str(datetime.now().strftime('%Y-%m-%d'))}"
        else:
            os.makedirs(f"./logs/{str(datetime.now().strftime('%Y-%m-%d'))}")
            save_folder = str(os.getcwd()) + f"./logs/{str(datetime.now().strftime('%Y-%m-%d'))}"

    if sys.platform == "win32":
        if os.path.isdir(f".\\logs\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"):
            save_folder = str(os.getcwd()) + f"\\logs\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"
        else:
            os.makedirs(f".\\logs\\{str(datetime.now().strftime('%Y-%m-%d'))}\\")
            save_folder = str(os.getcwd()) + f"\\logs\\{str(datetime.now().strftime('%Y-%m-%d'))}\\"

    # filename = save_folder + str(datetime.now().strftime("%H-%M-%S") +f'-{identifier}.txt')
    filename = str(save_folder) + str(db.identifier) + ".txt"

    with open(filename,"a+") as f:
        f.write(str(e))