from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(title="Open File",
                                          filetypes= (("text file","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,"r")
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openfile)
button.pack()
window.mainloop()