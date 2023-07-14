from tkinter import *
from tkinter import ttk 

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)
tab5 = Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.add(tab4,text="Tab 4")
notebook.add(tab5,text="Tab 5")
notebook.pack(expand=True,fill="both")

Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
Label(tab2,text="Hello, this is tab#2",width=50,height=25).pack()
Label(tab3,text="Hello, this is tab#3",width=50,height=25).pack()
Label(tab4,text="Hello, this is tab#4",width=50,height=25).pack()
Label(tab5,text="Hello, this is tab#5",width=50,height=25).pack()

window.mainloop()