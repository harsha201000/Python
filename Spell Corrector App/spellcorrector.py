from tkinter import *
from textblob import TextBlob

def clear():
    word1_field.delete(0,END)
    word2_field.delete(0,END)
    
def correction():
    input_word = word1_field.get()
    blob_obj = TextBlob(input_word)
    
    corrected_word = str(blob_obj.correct())
    
    word2_field.insert(10,corrected_word)

app = Tk()
app.title("Grammarly Spell Corrector")
app.geometry("400x200")

app.config(background='lightgreen')

grammarly = PhotoImage(file='grammarly.png')
grammarly_small = PhotoImage(file='grammarly-small.png')
clear_photo = PhotoImage(file='clear.png')
correct = PhotoImage(file='correct.png')
app.iconphoto(True,grammarly)

heading = Label(app,text="Welcome to Grammarly Spell Corrector App",fg="black",bg="forestgreen",font=('Arial',8,'bold'),image=grammarly_small,compound=RIGHT)
input_word = Label(app,text="Input Word",fg="black",bg="green")
corrected_word = Label(app,text="Corrected Word",fg="black",bg="green")

heading.grid(row=0,column=1)
input_word.grid(row=1,column=0)
corrected_word.grid(row=3,column=0,padx=10)

word1_field = Entry(bg="lightgrey")
word2_field = Entry(bg="lightgrey")

word1_field.grid(row=1,column=1,padx=10,pady=10)
word2_field.grid(row=3,column=1,padx=10,pady=10)

correct_word = Button(app,text="Correct Word",bg="yellowgreen",height=15,fg="black",image=correct,compound=RIGHT,command=correction)
clear_btn = Button(app,text="Clear",bg="orangered",height=15,fg="black",image=clear_photo,compound=RIGHT,command=clear)

correct_word.grid(row=2,column=1)
clear_btn.grid(row=4,column=1)


app.mainloop()