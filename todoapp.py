from tkinter import *
from tkinter import messagebox

task_list = []
counter = 1

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error","You haven't entered any task")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0,END)
    
def clear_taskField():
    enterTaskField.delete(0,END)
    
def add_task():
    global counter
    value = inputError()
    
    if value == 0:
        return
    
    content = enterTaskField.get() + "\n"
    
    task_list.append(content)
    
    textarea.insert('end -1 chars', " [ " + str(counter) + " ] " + content)
    
    counter += 1
    
    clear_taskField()
    
def remove_task():
    global counter
    
    if len(task_list) == 0:
        messagebox.showerror("No task")
        return
    
    number = taskNumberField.get(1.0,END)
    
    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)
        
    clear_taskNumberField()
    
    task_list.pop(task_no - 1)
    
    counter -= 1
    
    textarea.delete(1.0,END)
    
    for i in range(len(task_list)):
        textarea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_list[i])
    
    
    
app = Tk()
app.title("Todo App")
app.geometry("250x300")

app.config(background="yellowgreen")

enterTasklbl = Label(app,text="Enter Your Task",background="yellowgreen")

enterTaskField = Entry(app)

submit = Button(app,text="Submit",fg="black",bg="lightgreen",command=add_task)

textarea = Text(app,height=5,width=20,font="Roboto 15")

task_number = Label(app,text="Delete Task Number",bg="lightblue")

taskNumberField = Text(app,height=1,width=2,font="Roboto 15")

delete = Button(app,text="Delete",fg="black",bg="red",command=remove_task)

exit_button = Button(app,text="Exit",foreground="black",background="orange",command=exit)

enterTasklbl.grid(row=0,column=2)

enterTaskField.grid(row=1,column=2,ipadx=50)

submit.grid(row=2,column=2)

textarea.grid(row=3,column=2,padx=10,sticky=W)

task_number.grid(row=4,column=2,pady=5)

taskNumberField.grid(row=5,column=2)

delete.grid(row=6,column=2,pady=5)

exit_button.grid(row=7,column=2)

app.mainloop()