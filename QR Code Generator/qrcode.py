from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")

qrcode_icon = PhotoImage(file='qrcode.png')
window.iconphoto(True,qrcode_icon)

notebook = ttk.Notebook(window)
notebook.pack()

frame1 = Frame(notebook, height=400, width=200, bg="white")
frame1.pack(fill="both", expand=True)

frame2 = Frame(notebook, height=400, width=200, bg="black")
frame2.pack(fill="both", expand=True)

style = ttk.Style()
style.theme_create("style", parent="alt", settings={"TNotebook.Tab" : {"configure": {"padding": [20,10],"font": ('Times','20','bold')}}})
style.theme_use("style")

notebook.add(frame1, text="Generate QR Code")
notebook.add(frame2, text="Read QR Code")

canvas1 = Canvas(frame1, width="400", height="300", relief=RIDGE, bd=2)
canvas1.pack(padx=10,pady=10)

canvas2 = Canvas(frame2, width="400", height="400", relief=RIDGE, bd=2)
canvas2.pack(padx=10,pady=10)

def generate():
    if data_entry.get() != '' and save_entry.get() != '':
        qr = pyqrcode.create(data_entry.get())
        img = qr.png(save_entry.get() + ".png", scale=5)
        info = Label(frame1, text="Generated QR code:", font=('ariel 15 bold'))
        info.place(x=60, y=40)
        img = Image.open(save_entry.get() + ".png")
        img = ImageTk.PhotoImage(img)
        canvas1.create_image(200, 180, image=img)
        canvas1.image = img
    else:
        info = Label(frame1, text="Please enter the data for QR code", font=("Arial",15,"bold"))
        info.place(x=80,y=140)

def selected():
    img_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=(("PNG File", "*.png"),("All Files", "*.*")))
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    canvas2.create_image(200, 190, image=img)
    canvas2.image = img
    d = decode(Image.open(img_path))
    data = d[0].data.decode()
    qrcode_data = Label(frame2, text=data, bg='gold', fg='black', font=('ariel 15 bold'), relief=GROOVE)
    qrcode_data.place(x=50, y=380)

data_label = Label(frame1, text="Enter Data:", font=('Arial',15,'bold'), bg='white')
data_label.place(x=61, y=330)

save_label = Label(frame1, text="Enter name \n to save with:", font=("Arial",15,"bold"), bg="white")
save_label.place(x=55, y=360)

data_entry = Entry(frame1, font=("Arial",15,"bold"), relief=GROOVE, bd=3)
data_entry.place(x=197, y=330)

save_entry = Entry(frame1, font=("Arial",15,"bold"), relief=GROOVE, bd=3)
save_entry.place(x=197, y=380)

button1 = Button(frame1, text="Generate", bg="black", fg="gold", font=("Arial",15,"bold"), relief=GROOVE, command=generate)
button1.place(x=85, y=425)

button2 = Button(frame1, text="Exit", bg="black", fg="gold", font=("Arial",15,"bold"), relief=GROOVE, command=window.destroy)
button2.place(x=225, y=425)

button3 = Button(frame2, text="Select Image", bg="black", fg="gold", font=("Arial",15,"bold"), relief=GROOVE, command=selected)
button3.pack(side=LEFT, padx=50, pady=5)

button4 = Button(frame2, text="Exit", bg="black", fg="gold", font=("Arial",15,"bold"), relief=GROOVE, command=window.destroy)
button4.pack(side=LEFT, padx=10, pady=5)

window.mainloop()