from tkinter import *
import pybase64
from tkinter import messagebox

def clear():
    text_box.delete(1.0,END)
    entry.delete(0,END)
    
def encrypt():
    secret = text_box.get(1.0,END)
    text_box.delete(1.0,END)
    if entry.get() == "Harsh@2010$":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        text_box.insert(END,secret)
    else:
        messagebox.showwarning("Wrong Password!", "Incorrect Password, Try Again")
        
def decrypt():
    secret = text_box.get(1.0,END)
    text_box.delete(1.0,END)
    if entry.get() == "Harsh@2010$":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        text_box.insert(END,secret)
    else:
        messagebox.showwarning("Wrong Password!", "Incorrect Password, Try Again")
    

window = Tk()
window.geometry("500x500")
window.title("Encryption/Decryption App")

lock = PhotoImage(file="lock.png")
window.iconphoto(True,lock)

frame = Frame(window)
frame.pack(pady=20)

encrypt_button = Button(frame,text="Encrypt",font=("Arial",20),command=encrypt)
encrypt_button.grid(row=0,column=0)

decrypt_button = Button(frame,text="Decrypt",font=("Arial",20),command=decrypt)
decrypt_button.grid(row=0,column=1,padx=20)

clear_button = Button(frame,text="Clear",font=("Arial",20),command=clear)
clear_button.grid(row=0,column=2)

encrypt_label = Label(window,text="Encrypt/Decrypt Text...",font=("Arial",15))
encrypt_label.pack()

text_box = Text(window,width=60,height=10)
text_box.pack(pady=10)

password_label = Label(window,text="Enter your password...",font=("Arial",15))
password_label.pack()

entry = Entry(window,font=("Arial",20),width=35,show="*")
entry.pack(pady=10)

window.mainloop()