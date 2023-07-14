from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()
window.geometry("420x420")
window.title("Colorchooser")
color_chooser_tool = PhotoImage(file='931784.png')
window.iconphoto(True,color_chooser_tool)
button = Button(text="click me" ,command=click)
button.pack()
window.mainloop()