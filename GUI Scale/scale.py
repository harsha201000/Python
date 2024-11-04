from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()
window.title("Scale")

hotImage = PhotoImage(file='icons8-hot-48.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,from_=100,to=0,length=500,orient=VERTICAL,font=('Consolas',20),tickinterval=10,resolution=5,troughcolor='lightblue',fg='orange',bg='black')
scale.set(scale['from']-scale['to']/2+scale['to'])
scale.pack()

coldImage = PhotoImage(file='icons8-cold-48.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()