from tkinter import *
import wikipedia

window = Tk()
window.geometry("700x700")
window.title("Wikipedia")

def clear():
    entry.delete(0,END)
    text.delete(0.0,END)
    
def search():
    data = wikipedia.page(entry.get())
    clear()
    text.insert(0.0, data.content)


wikipedia_logo = PhotoImage(file='icons8-wikipedia-80.png')
window.iconphoto(True,wikipedia_logo)

label_frame = LabelFrame(window, text="Search")
label_frame.pack(pady=20)

entry = Entry(label_frame, font=("Sans-serif",20),width=50)
entry.pack(pady=20,padx=20)

frame = Frame(window)
frame.pack(pady=5)

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

horizontal_scroll = Scrollbar(frame,orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)

text = Text(frame, yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=horizontal_scroll.set)
text.pack()

text_scroll.config(command=text.yview)
horizontal_scroll.config(command=text.xview)

button_frame = Frame(window)
button_frame.pack(pady=10)

search_button = Button(button_frame,text="Lookup",font=("Helvetica",32),fg='#3a3a3a',command=search)
search_button.grid(row=0,column=0,padx=20)

clear_button = Button(button_frame,text="Clear",font=("Helvetica",32),fg='#3a3a3a',command=clear)
clear_button.grid(row=0,column=1)

window.mainloop()