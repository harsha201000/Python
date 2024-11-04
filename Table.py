# Python program to create a table
from tkinter import *

class Table:
    
    def __init__(self,root):
        
        # code for creating a table
        for x in range(total_rows):
            for y in range(total_columns):
                self.entry = Entry(root,width=20,fg='green',font=("Arial",20,"bold"))
                self.entry.grid(row=x,column=y)
                self.entry.insert(END,lst[x][y])
                
# Take the data
lst = [(1,'Siva Malipeddi',42),
       (2,'Durga Malipeddi',40),
       (3,'Harsha Malipeddi',13),
       (4,'Havisha Malipeddi',10)]

total_rows = len(lst)
total_columns = len(lst[0])

window = Tk()
window.title("Family Ages Table")
table = Table(window)
window.mainloop()