from tkinter import * 



def display():
    if (x.get()==0):
        print("You agree")
    else:
        print("You don't agree")

window = Tk()
window.title("Checkbox")

x = IntVar()

python_photo = PhotoImage(file='Python.png')
icon = PhotoImage(file='Python.png')

window.iconphoto(True,icon)

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=0,
                           offvalue=1,
                           command=display,
                           font=('Arial',20),
                           fg='green',
                           bg="black",
                           activeforeground='green',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound="left")
check_button.pack()
window.mainloop()