from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox

app = Tk()
count = 0

def generate():
    global comp
    comp = random.randint(0,100)
    
def basic():
    app.title("Number Guessing Game")
    app.geometry("500x500")
    app.minsize(500,500)
    app.maxsize(500,500)
    app.config(background="grey")
    photo = PhotoImage(file='guess.png')
    app.iconphoto(False,photo)
    heading = Label(text="Number Guessing Game",font="Helvetica 18 bold",bg="black",fg="tomato",padx=170)
    heading.pack()
    with open('score.txt','r') as f:
        hg = f.read()
    sc = Label(app,text=f'Previous score: {hg}',font="lucida 8 bold")
    sc.pack(anchor=E,padx=25,pady=5)
    
    footer = Label(text="Developed by Harsha Malipeddi",font="Helvetica 8 bold",bg="black",fg="tomato",padx=153)
    footer.pack(side=BOTTOM)
    
    menu = Menu(app)
    file = Menu(menu,tearoff=0)
    menu.add_cascade(label="Start",menu=file)
    menu.add_cascade(label="Restart",command=restart)
    menu.add_command(label="About",command=about)
    menu.add_command(label="Quit",command=quit)
    app.config(menu=menu)
    generate()
    
def result():
    global count
    number = userv.get()
    if number == "":
        messagebox.showerror('Error', "Please enter a value")
    else:
        n = int(number)
        count += 1
        if count == 10:
            a = messagebox.showinfo("Game Over", "You lost the game")
        elif comp == n:
            score = 11-count
            a = messagebox.showinfo('Win',f'You guess right number!\n Your score {score}')
            show.config(text="Win!",fg="green")
            with open("score.txt","w") as f:
                f.write(str(score))
            generate()
            messagebox.showinfo("Next Number",f"click ok to guess another number")
        elif comp > n:
            show.config(text="Select greater number",fg="green")
        else:
            show.config(text="Select smaller number",fg="red")
            
def restart():
    messagebox.showerror("Reset","Game Reset!")
    
def about():
    str1 = 'This game is developed by Python VSCode\n\ncopyright@2023'
    messagebox.showinfo('About',str1)
    
basic()

userv = StringVar()
user = Entry(app,textvariable=userv,justify=CENTER,relief=FLAT,borderwidth=2,font="Helvetica 18 bold")
user.pack(pady=10)

i = Image.open('guess.png',mode='r')
img = ImageTk.PhotoImage(i)
l = Label(image=img)
l.pack(pady=30)
i = Image.open('bt.png')
resized_image = i.resize((150, 50), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
submit = Button(app,image=new_image,command=result,font="Helvetica 18 bold",relief=FLAT)
submit.pack(pady=10)
show = Label(app,text='',font='Helvetica 12 bold')
show.pack(pady=10)

app.mainloop()
    
