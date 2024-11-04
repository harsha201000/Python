from tkinter import *
from tkinter import messagebox
def submit():
    messagebox.showinfo("Status", "Successfully registered into python")

def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)

def newwindow():
    window2 = Tk()
    lbl = Label(window2, text="Welcome to Codeyoung")
    lbl.pack()
    window2.mainloop()

def select():
    sel = "Value = " + str(v.get())
    label.config(text=sel)

window = Tk()
window.title("Codeyoung GUI App")
window.geometry("800x600")
window.config(bg="orange")

v = DoubleVar()  # Define v here

# First section
lbl = Label(window, text="Welcome to Codeyoung", fg="purple", bg="white")
lbl.grid(row=0, column=0, columnspan=2)

lbl1 = Label(window, text="You have successfully enrolled into python programming language.", fg="yellow", bg="black")
lbl1.grid(row=1, column=0, columnspan=2)

# Second section
fn = Label(window, text="Enter your first name")
fn.grid(row=2, column=0)
fe = Entry(window)
fe.grid(row=2, column=1)

ln = Label(window, text="Enter your last name")
ln.grid(row=3, column=0)
le = Entry(window)
le.grid(row=3, column=1)

em = Label(window, text="Enter your email id")
em.grid(row=4, column=0)
ee = Entry(window)
ee.grid(row=4, column=1)

btn_submit = Button(window, text="Submit", command=submit)
btn_submit.grid(row=5, column=1)

# Third section
lbl_fav_lang = Label(window, text="Favorite Programming Language")
lbl_fav_lang.grid(row=6, column=0, columnspan=2)

radio = IntVar()
langs = ["Python", "Java", "C", "C++", "C#", "Web Dev"]
for i, lang in enumerate(langs):
    Radiobutton(window, text=lang, variable=radio, value=i+1, command=selection).grid(row=i+7, column=0, sticky=W)

label = Label(window)
label.grid(row=13, column=0, columnspan=2)

# Fourth section
text = Text(window)
text.insert(INSERT, "Name.....")
text.insert(END, "Salary.....")
text.grid(row=14, column=0, columnspan=2)

text.tag_add("Write Here", "1.0", "1.4")
text.tag_add("Click Here", "1.8", "1.13")
text.tag_config("Write Here", background="yellow", foreground="black")
text.tag_config("Click Here", background="black", foreground="white")

# Fifth section
btn_new_window = Button(window, text="Open New Window", command=newwindow)
btn_new_window.grid(row=15, column=0)

spin = Spinbox(window, from_=0, to=10)
spin.grid(row=15, column=1)

# Sixth section
lblfrm_python_course = LabelFrame(window, text="Python Course")
lblfrm_python_course.grid(row=16, column=0, columnspan=2, sticky="ew")
lbl1 = Label(lblfrm_python_course, text="Python Basic, Python Advanced, Data Science, Machine Learning, AI")
lbl1.pack()

lblfrm_web_dev_course = LabelFrame(window, text="Web Development Course")
lblfrm_web_dev_course.grid(row=17, column=0, columnspan=2, sticky="ew")
lbl2 = Label(lblfrm_web_dev_course, text="HTML, JAVASCRIPT, CSS, REACTJS, NODEJS, ANGULARJS, BOOTSTRAP, MONGODB")
lbl2.pack()

# Seventh section
menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete")
edit_menu.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About")
menubar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menubar)

# Eighth section
frame = Frame(window)
frame.grid(row=18, column=0, columnspan=2)

btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=LEFT)

btn3 = Button(frame, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(frame, text="Modify", fg="black", activebackground="white")
btn4.pack(side=LEFT)

# Ninth section
btn_submit_msg = Button(window, text="Submit", command=submit)
btn_submit_msg.grid(row=19, column=0)

# Tenth section
lbl_select_fruit = Label(window, text="Select your favorite fruit")
lbl_select_fruit.grid(row=19, column=1)
check_var = IntVar()
btn_apple = Checkbutton(window, text="Apple", variable=check_var, onvalue=1, offvalue=0, height=2, width=0)
btn_apple.grid(row=20, column=1)

# Eleventh section
scale = Scale(window, variable=v, from_=1, to=50, orient=HORIZONTAL)
scale.grid(row=21, column=0, columnspan=2)

btn_scale = Button(window, text="Value", command=select)
btn_scale.grid(row=22, column=0, columnspan=2)

label = Label(window)
label.grid(row=23, column=0, columnspan=2)

# Twelfth section
sb = Scrollbar(window)
sb.grid(row=24, column=1, sticky="ns")

mylist = Listbox(window, yscrollcommand=sb.set)
for line in range(50):
    mylist.insert(END, "No. " + str(line))
mylist.grid(row=24, column=0, sticky="nsew")
sb.config(command=mylist.yview)

# Thirteenth section
lbl_course = Label(window, text="Leave a list of programs that you are looking forward to enrolling")
lbl_course.grid(row=25, column=0, columnspan=2)

lst = Listbox(window)
lst.insert(1, "Python Level 1")
lst.insert(2, "Python Level 2")
lst.insert(3, "Python Level 3")
btn_del = Button(window, text="Delete", command=lambda: lst.delete(ANCHOR))

lst.grid(row=26, column=0, columnspan=2)
btn_del.grid(row=27, column=0, columnspan=2)

window.mainloop()