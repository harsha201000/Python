from tkinter import *

def calc_hypotenuse():
    a = float(leg1_entry.get())
    b = float(leg2_entry.get())
    c = (a**2 + b**2)**0.5
    hypotenuse_lbl.config(text=f"Hypotenuse = {c:.2f}")

def clear():
    leg1_entry.delete(0,END)
    leg2_entry.delete(0,END)
    hypotenuse_lbl.config(text=f"Hypotenuse = ")

window = Tk()
window.title("Pythagorean Theorem Calculator")


leg1_lbl = Label(window,text="Enter length of side 1 : ")
leg1_lbl.grid(row=0,column=0,padx=5,pady=5)

leg1_entry = Entry(window)
leg1_entry.grid(row=0,column=1,padx=5,pady=5)

leg2_lbl = Label(window,text="Enter length of side 2 : ")
leg2_lbl.grid(row=1,column=0,padx=5,pady=5)

leg2_entry = Entry(window)
leg2_entry.grid(row=1,column=1,padx=5,pady=5)

hypotenuse_lbl = Label(window,text="Hypotenuse = ")
hypotenuse_lbl.grid(row=2,columnspan=2,padx=5,pady=5)

calc_hypotenuse_btn = Button(window,text="Calculate Hypotenuse",bg="green",font="Aptos 10 bold",command=calc_hypotenuse)
calc_hypotenuse_btn.grid(row=3,column=2,padx=5,pady=5)

clear_btn = Button(window,text="Clear All",bg="red",font="Aptos 10 bold",command=clear)
clear_btn.grid(row=3,column=1,padx=5,pady=5)


window.mainloop()