import tkinter as tk
import turtle as tl
import os


def question(question, title):
    screen = tl.getscreen()
    return screen.textinput(title, question)
def Onstart():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    filename2 = filename.split('/')
    filenamelen = len(filename2)
    global a1
    a1 = filename2[filenamelen-1]
    import copy
    filename4 = copy.deepcopy(filename2)
    del filename4[filenamelen-1]
    filename5 = "/".join(filename4)
    os.chdir(filename5)
    list1 = list()
    titre = question('Votre question', 'I-DREAM QUIZZ 1.0')
    r1 = question('réponce 1 ', 'I-DREAM QUIZZ 1.0')
    r2 = question('réponce 2', 'I-DREAM QUIZZ 1.0')
    r3 = question('réponce 3 ', 'I-DREAM QUIZZ 1.0')
    rc = question('réponce correcte = n° ', 'I-DREAM QUIZZ 1.0')
    list1.append(titre)
    list1.append(r1)
    list1.append(r2)
    list1.append(r3)
    list1.append(rc)
    return list1
def Write(what, title):
    file = open(title, mode='w')
    file.write(what[0] + '\n')
    file.write(what[1] + '\n')
    file.write(what[2] + '\n')
    file.write(what[3] + '\n')
    file.write(what[4] + '\n')
a = Onstart()
Write(a, a1)
