from tkinter import *

def get_percentile():
    students = int(total_participantField.get())
    rank = int(rankField.get())
    
    result = round((students - rank) / students * 100,3)
    
    percentileField.insert(10,str(result))
    
def clear():
    rankField.delete(0,END)
    total_participantField.delete(0,END)
    percentileField.delete(0,END)

gui = Tk()
gui.geometry("600x250")
gui.title("Rank Based - Percentile Calculator")
gui.config(background="lightgreen")

rank = Label(gui,text="Rank",bg="lightblue")
andl = Label(gui,text="And",bg="lightblue")
total_participant = Label(gui,text="Total Participants",bg="lightblue")
find = Button(gui,text="Find Percentile",fg="black",bg="white",command=get_percentile)
percentile = Button(gui,text="Percentile",fg="black",bg="white")
clear = Button(gui,text="Clear",fg="black",bg="red",command=clear)

rank.grid(row=1,column=1,padx=10)
andl.grid(row=1,column=4)
total_participant.grid(row=1,column=6,padx=10)

find.grid(row=3,column=4,padx=10)
percentile.grid(row=4,column=3,padx=10)
clear.grid(row=5,column=4,padx=10)

rankField = Entry(gui)
total_participantField = Entry(gui)
percentileField = Entry(gui)

rankField.grid(row=1,column=2)
total_participantField.grid(row=1,column=7)
percentileField.grid(row=4,column=4)

gui.mainloop()