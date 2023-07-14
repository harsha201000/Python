from tkinter import *

fruits = ["apple", "banana"]

def order():
    if(x.get()==0):
        print("you ordered apple!")
    elif (x.get()==1):
        print("you ordered banana")
    else:
        print("huh?")

window = Tk()
window.title("Radiobuttons")

appleImage = PhotoImage(file='apple.png')
bananaImage = PhotoImage(file='banana.png')
fruitImages = [appleImage,bananaImage]

x = IntVar()

for index in range(len(fruits)):
    radiobutton = Radiobutton(window,text=fruits[index],variable=x,value=index,padx=25,font=("Impact",50),image=fruitImages[index],compound="left",indicatoron=0,width=375,command=order)
    radiobutton.pack(anchor=W)

window.mainloop()