from tkinter import *

# Function
def getinfo():
    print("Approved")

# Create a window
window = Tk()
window.geometry("500x300")
# Set the window title
window.title("Login in Python")

# set the iconphoto and the image for the header
python = PhotoImage(file='python.png')
window.iconphoto(True,python)

# Header
label = Label(window,text="Python Registeration Form",font="Arial 15 bold",image=python,compound=RIGHT)
label.grid(row=0,column=3)

# Field
name = Label(window,text="Name")
email = Label(window,text="Email")
phonenumber = Label(window,text="Phone")
gender = Label(window,text="Gender")

# Packings
name.grid(row=1,column=2)
email.grid(row=2,column=2)
phonenumber.grid(row=3,column=2)
gender.grid(row=4,column=2)

# Values
namevalue = StringVar
emailvalue = StringVar
phonenumbervalue = StringVar
gendervalue = StringVar
checkvalue = IntVar

# Entry
name_entry = Entry(window,textvariable=namevalue,width=40)
email_entry = Entry(window,textvariable=emailvalue,width=40)
phonenumber_entry = Entry(window,textvariable=phonenumbervalue,width=40)
gender_entry = Entry(window,textvariable=gendervalue,width=40)

# Packings
name_entry.grid(row=1,column=3)
email_entry.grid(row=2,column=3)
phonenumber_entry.grid(row=3,column=3)
gender_entry.grid(row=4,column=3)

# Create check button
checkbtn = Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)

# Create submit button
submit_button = Button(text="Submit", command=getinfo)
submit_button.grid(row=7,column=3)

window.mainloop()