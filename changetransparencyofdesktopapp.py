from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("500x500")

window.attributes('-alpha', 1)

label = Label(window,text="Hello World",font=("Arial",25))
label.pack(pady=20)

def slide(x):
    window.attributes('-alpha',slider.get())
    slide_label.config(text=str(round(slider.get(),2)))
    
def new_desktop():
    global new
    new = Toplevel()
    new.attributes('-alpha', 0.5)

slider = Scale(window, from_=0.1, to=1, value=0.7, orient=HORIZONTAL, command=slide)
slider.pack(pady=20)

slide_label = Label(window, text='Slide')
slide_label.pack(pady=10)

new_window = Button(window, text="New Window",command=new_desktop)
new_window.pack()


window.mainloop()