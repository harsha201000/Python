from tkinter import *
from tkcalendar import *

window = Tk()

def select_date():
    date = cal.get_date()
    selected_date = Label(text=date)
    selected_date.pack(padx=2,pady=2)

cal = Calendar(window,setmode="day",date_pattern='d/m/yy')
cal.pack(padx=15,pady=15)

open_cal = Button(window,text="select date",command=select_date)
open_cal.pack(padx=15,pady=15)

window.geometry("300x300")
window.title("Calendar")
window.configure(bg="lightblue")

calendar_icon = PhotoImage(file='calendar_logo.png')
window.iconphoto(True,calendar_icon)

window.mainloop()