from tkinter import *
import pyshorteners

window = Tk()
window.geometry("500x500")
window.title("Link Shortener")

def shorten_link():
    if shorten.get():
        shorten.delete(0,END)
    
    if entry.get():
        url = pyshorteners.Shortener().tinyurl.short(entry.get())
        shorten.insert(END,url)
        
        print(pyshorteners.Shortener().tinyurl.expand(url))

label = Label(window,text="Enter a link to shorten",font=("Russo One",30))
label.pack(pady=20)

entry = Entry(window,font=("Russo One",25))
entry.pack(pady=20)

button = Button(window,text="Shorten Link",command=shorten_link,font=("Russo One",25))
button.pack(pady=20)

shorten_label = Label(window,text="Shortened Link",font=("Russo One",15))
shorten_label.pack(pady=20)

shorten = Entry(window,font=("Helvetica",15),justify=CENTER,width=30,bd=0,bg="systembuttonface")
shorten.pack(pady=10)

window.mainloop()