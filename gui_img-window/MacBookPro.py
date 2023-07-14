import tkinter as tk

window = tk.Tk()
window.title("MacBook Pro")
window.geometry("500x500")
window.config(bg="grey")

apple = tk.PhotoImage(file='icons8-apple-logo-16.png')
window.iconphoto(True, apple)

macbook_pro = tk.PhotoImage(file='macbookpro16inch-2019.png')

img = tk.Label(window,text="MacBook Pro 16-inch 2019",font=("Arial", 25, "bold"), fg="lightgrey", bg="gray",border=20, relief=tk.RAISED, padx=120, pady=120, image=macbook_pro,compound='top')
img.place(x=0, y=0)
img.pack()


window.mainloop()