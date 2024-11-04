from tkinter import *

# Checkbox
window = Tk()
window.geometry("202x239")
window.title("Choose your programming language")

program_img = PhotoImage(file="programmer.png")
window.iconphoto(True,program_img)

def selectedC():
    print("You have selected C")
    
def selectedCPP():
    print("You have selected C++")
    
def selectedJava():
    print("You have selected Java")
    
def selectedPython():
    print("You have selected Python")
    
def selectedCSharp():
    print("You have selected C#")
    
def selectedWebDev():
    print("You have selected Web Devlopment")

label = Label(window,text="Favorite Programming Language")
label.pack()
check_var = IntVar()
btn = Checkbutton(window,text="C",variable=check_var,onvalue=1,offvalue=0,height = 2,width = 0,command=selectedC)
btn.pack()
btn1 = Checkbutton(window,text="C++",variable=check_var,onvalue=2,offvalue=0,height = 2, width = 0,command=selectedCPP)
btn1.pack()
btn2 = Checkbutton(window,text="Java",variable=check_var,onvalue=3,offvalue=0,height = 2, width = 0,command=selectedJava)
btn2.pack()
btn3 = Checkbutton(window,text="Python",variable=check_var,onvalue=4,offvalue=0,height = 2, width = 0,command=selectedPython)
btn3.pack()
btn4 = Checkbutton(window,text="C#",variable=check_var,onvalue=5,offvalue=0,height = 2, width = 0,command=selectedCSharp)
btn4.pack()
btn5 = Checkbutton(window,text="Web Devlopment",variable=check_var,onvalue=6,offvalue=0,height = 2, width = 0,command=selectedWebDev)
btn5.pack()



window.mainloop()