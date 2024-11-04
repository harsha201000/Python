from tkinter import *
from datetime import datetime
from tkinter import messagebox

window = Tk()
window.geometry("500x300")
window.title("Age Calculator")

def calculate_age():
    if entry.get():
        current_year = datetime.now().year
        your_age = current_year - int(entry.get())
        if your_age < 0:
            messagebox.showerror("TypeError", "You entered the wrong DOB")
        else:
            messagebox.showinfo("Your age", "Your age is {}".format(your_age))
            
    else:
        messagebox.showerror("Error", "You forgot to enter your age!")

label = Label(window, text="Enter Year Born", font=("Helvetica",24))
label.pack()

entry = Entry(window, font=("Helvetica",18))
entry.pack()

button = Button(window, text="Calculate your age", font=("Helvetica",18), command=calculate_age)
button.pack()

window.mainloop()