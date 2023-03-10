from tkinter import *
import os

def Onstart():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    filename2 = filename.split('/')
    filenamelen = len(filename2)
    global file
    file = filename2[filenamelen-1]
    import copy
    filename4 = copy.deepcopy(filename2)
    del filename4[filenamelen-1]
    filename5 = "/".join(filename4)
    os.chdir(filename5)
    fichier = open(file, mode='wb')
    line0 = fichier.read().splitlines()
    return line0



def INIT():
    list2 = Onstart()
    def correction():
        if answer==list2[4]:
            print('Correct')
        else:
            print('Faux')
        master.destroy()
        input()

    global answer
    answer = 0
    def c1():
        global answer
        answer = '1'
    def c2():
        global answer
        answer = '2'
    def c3():
        global answer
        answer = '3'
    master = Tk()
    master.title(list2[0])
    var0 = IntVar()
    Checkbutton(master, text=list2[0], variable=var0).grid(row=1, sticky=N)
    var1 = IntVar()
    Checkbutton(master, text=list2[1], variable=var1, command=c1).grid(row=3, sticky=N)
    var2 = IntVar()
    Checkbutton(master, text=list2[2], variable=var2, command=c2).grid(row=4, sticky=N)
    var3 = IntVar()
    Checkbutton(master, text=list2[3], variable=var3, command=c3).grid(row=5, sticky=N)
    var4 = IntVar()
    Checkbutton(master, text='Correction', variable=var4, command=correction).grid(row=6, sticky=N)
    master.mainloop()
INIT()

