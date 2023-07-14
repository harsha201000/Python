from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Harsha First GUI program")
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="green")

window.mainloop()