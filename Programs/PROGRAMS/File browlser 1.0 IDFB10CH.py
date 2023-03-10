# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window
def dele():
    from tkinter import messagebox
 
    messagebox.showwarning("Attention", "Ce fichier va etre suprimé déffinitivement")
    import os
    filename2 = filename.split('/')
    filenamelen = len(filename2)
    a1 = filename2[filenamelen-1]
    import copy
    filename4 = copy.deepcopy(filename2)
    del filename4[filenamelen-1]
    filename5 = "/".join(filename4)
    os.chdir(filename5)
    print(os.getcwd())
    os.remove(a1)
    messagebox.showinfo('Successful','Vous avez essayer de suprimé : ' + a1)
    messagebox.showinfo('Successfuly deleted',a1 + '   a été suprimé')
def remplace():
    import os
    filename2 = filename.split('/')
    filenamelen = len(filename2)
    a1 = filename2[filenamelen-1]
    import copy
    filename4 = copy.deepcopy(filename2)
    del filename4[filenamelen-1]
    filename5 = "/".join(filename4)
    os.chdir(filename5)
    import turtle as tl
    screen = tl.getscreen()
    a2 = screen.textinput('Name', 'Rename file')
    os.replace(a1, a2)
def browseFiles():
    global filename
    filename = filedialog.askopenfilename()
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
      
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  

button_op = Button(window,
                     text = "DELETE",
                     command = dele)
button_ren = Button(window,
                     text = "Renomer",
                     command = remplace)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_op.grid(column = 1,row = 50)
button_ren.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()
