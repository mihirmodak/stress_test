from tkinter import *

import variables as master_db; master_db.init()
global identifier
identifier= master_db.identifier

def init(stroop_root):
    global root
    root = stroop_root

    global file # The file to save

    global compatible
    comptaible = None

    global options # The possible options for color / word
    options = ('green', 'blue', 'yellow', 'red')
    # global old_color
    # old_color = "none"
    # global old_word
    # old_word = "NONE"

    global trials # Necessary for Submit and Questions functions
    trials = 0

    global start_button # To begin the test

    global timer
    global label_t # The label for the timer
    lebel_t = Label()

    global diffic_easy
    diffic_easy = IntVar()
    global diffic_med
    diffic_med = IntVar()
    global diffic_hard
    diffic_hard = IntVar()
    global congruent_prop # the % of colors that match the words, i.e. color=green, word="GREEN"

    global checkbox1
    checkbox1 = Checkbutton()
    global checkbox2
    checkbox2 = Checkbutton()
    global checkbox3
    checkbox3 = Checkbutton()

    global instructions
    instructions = Label()

    global entryWidget
    entryWidget = Entry()