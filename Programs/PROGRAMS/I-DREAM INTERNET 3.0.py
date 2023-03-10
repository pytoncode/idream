import os
import turtle as tl
import webbrowser

def _init_search():
    from turtle import getscreen
    screen = getscreen()
    search = screen.textinput('I-DREAM INTERNET 2.2','search')
    return search
def init(site1, site2, site3, site4, site5, site6, site7, site8, site9, site10):
    import tkinter as tk
    r = tk.Tk()
    r.title('I-DREAM INTERNET 2.2')
    button1 = tk.Button(r, text=site1, width=100, command=opensite1)
    button2 = tk.Button(r, text=site2, width=100, command=opensite2)
    button3 = tk.Button(r, text=site3, width=100, command=opensite3)
    button4 = tk.Button(r, text=site4, width=100, command=opensite4)
    button5 = tk.Button(r, text=site5, width=100, command=opensite5)
    button6 = tk.Button(r, text=site6, width=100, command=opensite6)
    button7 = tk.Button(r, text=site7, width=100, command=opensite7)
    button8 = tk.Button(r, text=site8, width=100, command=opensite8)
    button9 = tk.Button(r, text=site9, width=100, command=opensite9)
    button10 = tk.Button(r, text=site10, width=100, command=opensite10)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    button9.pack()
    button10.pack()

def init2(site1, site2):
    import tkinter as tk
    r = tk.Tk()
    r.title('I-DREAM INTERNET 2.2')
    button1 = tk.Button(r, text=site1, width=100, command=opensite1)
    button2 = tk.Button(r, text=site2, width=100, command=opensite2)
    button1.pack()
    button2.pack()












    
def opensite1():
    import webbrowser
    webbrowser.open(site[1], new=2)
def opensite2():
    import webbrowser
    webbrowser.open(site[2], new=2)
def opensite3():
    import webbrowser
    webbrowser.open(site[3], new=2)
def opensite4():
    import webbrowser
    webbrowser.open(site[4], new=2)
def opensite5():
    import webbrowser
    webbrowser.open(site[5], new=2)
def opensite6():
    import webbrowser
    webbrowser.open(site[6], new=2)
def opensite7():
    import webbrowser
    webbrowser.open(site[7], new=2)
def opensite8():
    import webbrowser
    webbrowser.open(site[8], new=2)
def opensite9():
    import webbrowser
    webbrowser.open(site[9], new=2)
def opensite10():
    import webbrowser
    webbrowser.open(site[9], new=2)
def recherche():
    b = _init_search()
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
 
    # to search
    z = 0
    global site
    site = list()
    for j in search(b, tld="co.in", num=10, stop=10, pause=0):
        site.append(j)
    print(site)
    
    try:
        init(site[0], site[1], site[2], site[3], site[4], site[5], site[6], site[7], site[8], site[9])
    except :
        init2(site[0], site[1], site[2])
        
recherche()
input()
