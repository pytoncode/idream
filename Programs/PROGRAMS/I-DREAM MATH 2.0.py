import turtle as tl
import tkinter
from tkinter import*

def restart():
    global num1
    global num2
    num1 = ''
    num2 = ''
    global opp
    opp = False
    global opp2
    opp2 = ''
restart()


def num1_1():
    global num1
    b = num1 + '1'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)

def num1_2():
    global num1
    b = num1 + '2'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_3():
    global num1
    b = num1 + '3'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_4():
    global num1
    b = num1 + '4'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_5():
    global num1
    b = num1 + '5'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_6():
    global num1
    b = num1 + '6'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_7():
    global num1
    b = num1 + '7'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_8():
    global num1
    b = num1 + '8'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_9():
    global num1
    b = num1 + '9'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num1_0():
    global num1
    b = num1 + '0'
    from copy import deepcopy
    num1 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_1():
    global num2
    b = num2 + '1'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_2():
    global num2
    b = num2 + '2'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_3():
    global num2
    b = num2 + '3'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_4():
    global num2
    b = num2 + '4'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_5():
    global num2
    b = num2 + '5'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_6():
    global num2
    b = num2 + '6'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    label.pack()
    
def num2_7():
    global num2
    b = num2 + '7'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_8():
    global num2
    b = num2 + '8'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_9():
    global num2
    b = num2 + '9'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)
    
def num2_0():
    global num2
    b = num2 + '0'
    from copy import deepcopy
    num2 = deepcopy(b)
    a = num1 + opp2 + num2
    label.config(text = a)


    
def chose0():
    global opp
    print(opp)
    if opp==True:
        num2_0()
    elif opp==False:
        num1_0()

def chose1():
    global opp
    if opp==True:
        num2_1()
    elif opp==False:
        num1_1()

def chose2():
    global opp
    if opp==True:
        num2_2()
    elif opp==False:
        num1_2()

def chose3() :
    global opp
    if opp==True :
        num2_3()
    elif opp==False :
        num1_3()

def chose4():
    global opp
    if opp==True:
        num2_4()
    elif opp==False:
        num1_4()

def chose5():
    global opp
    if opp==True:
        num2_5()
    elif opp==False:
        num1_5()

def chose6():
    global opp
    if opp==True:
        num2_6()
    elif opp==False:
        num1_6()

def chose7():
    global opp
    if opp==True:
        num2_7()
    elif opp==False:
        num1_7()

def chose8():
    global opp
    if opp==True:
        num2_8()
    elif opp==False:
        num1_8()

def chose9():
    global opp
    if opp==True:
        num2_9()
    elif opp==False:
        num1_9()

def opp1():
    global opp
    opp = True
def oppplu():
    global opp2
    opp2 = '+'
    opp1()
def oppmoi():
    global opp2
    opp2 = '-'
    opp1()
def oppdiv():
    global opp2
    opp2 = '/'
    opp1()
def oppmul():
    global opp2
    opp2 = '*'
    opp1()

def truc(evenement):
    evenement.keysym
    label.pack()
    print(num1)
    print(opp2)
    print(num2)
def calc():
    global opp2
    global num1
    global num2
    if opp2=='+':
        z = int(num1) + int(num2)
    elif opp2=='-':
        z = int(num1) - int(num2)
    elif opp2=='/':
        z = int(num1) / int(num2)
    elif opp2=='*':
        z = int(num1) * int(num2)
    az = 'Le résulatat est :' + str(z)
    label.config(text = az)



























































































    
f = tkinter.Tk(screenName='I-DREAM math 2.0')
c = tkinter.Canvas(f, width=50, height=50)
label = Label(f, text='I-DREAM Math')
button1 = tkinter.Button(c, text=1, command=chose1)
button2 = tkinter.Button(c, text=2, command=chose2)
button3 = tkinter.Button(c, text=3, command=chose3)
button4 = tkinter.Button(c, text=4, command=chose4)
button5 = tkinter.Button(c, text=5, command=chose5)
button6 = tkinter.Button(c, text=6, command=chose6)
button7 = tkinter.Button(c, text=7, command=chose7)
button8 = tkinter.Button(c, text=8, command=chose8)
button9 = tkinter.Button(c, text=9, command=chose9)
button0 = tkinter.Button(c, text=0, command=chose0)
buttonx = tkinter.Button(c, text='Multiplier par ', command=oppmul)
buttond = tkinter.Button(c, text='Diviser par', command=oppdiv)
buttonm = tkinter.Button(c, text='moins', command=oppmoi)
buttonp = tkinter.Button(c, text='plus', command=oppplu)
buttonc = tkinter.Button(c, text='Calculer', command=calc)
buttonre = tkinter.Button(c, text='Restart', command=restart)
button0.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
buttonp.pack()
buttonm.pack()
buttond.pack()
buttonx.pack()
buttonc.pack()
buttonre.pack()

label.pack()
c.pack()
c.bind_all('<Key>', truc)
c.mainloop




