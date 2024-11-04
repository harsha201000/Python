from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir='c:\\Users\\Harsha\\Documents\\',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("Rich Text Format file",".rtf"),
                                        ("All files",".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="save",command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()