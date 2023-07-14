from tkinter import *


def submit():
    input = text.get("1.0",END)
    print(input)
window = Tk()
icon = PhotoImage(file='82071.png')
window.iconphoto(True,icon)
window.title("Notepad Text")
text = Text(window,
            bg="white",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="green")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()