from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This is an info message box", message= "You are a person")
    #messagebox.showwarning(title="WARNING!", message= "Your computer has a virus!")
    #messagebox.showerror(title="ERROR!", message= "Something went wrong!")
    
    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to visit a app?'):
        #print("You visited an app")
    #else:
        #print("You closed a app")
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry a app?'):
        #print("You retried an app")
    #else:
        #print("You closed a app")
        
    #if messagebox.askyesno(title='ask yes or no',message="Do you like coding?"):
        #print("I like coding") 
    #else:
        #print("Why dont you like coding?")
        
    #answer = messagebox.askquestion(title='ask question',message='Do you like to play inside?')
    #if (answer == 'yes'):
        #print("I like to play inside")
    #else:
        #print("Why dont you play inside?")
        
    answer = messagebox.askyesnocancel(title=' Yes no cancel', message="Do you like to program?",icon='info')
    if (answer==True):
        print("You like to program.")
    elif(answer==False):
        print("Why dont you practice basics of coding.")
    else:
        print("You have closed the question.")
window = Tk()

button = Button(window,command=click,text="click me")
button.pack()

window.mainloop()