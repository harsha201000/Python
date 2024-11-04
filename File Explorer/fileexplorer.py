from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("File Explorer")
window.geometry("550x500")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes= (("Text Files","*.txt*"),("All Files","*.*")))
    file_explorer_heading.configure(text="File Opened {}".format(filename))

window.config(background="white")

file = PhotoImage(file="explorer.png")
window.iconphoto(True,file)

file_explorer_heading = Label(window,text="File Explorer using Tkinter",width=100,height=4,fg="blue")

explore = Button(window,text="Browse Files",command=browseFiles)

exit_button = Button(window,text="Exit",command=exit)

file_explorer_heading.grid(row=1,column=1)
explore.grid(row=2,column=1)
exit_button.grid(row=3,column=1)

window.mainloop()