#import all the required libraries
from tkinter import *
import math


#create a class called as calc
class Calculator:
  def __init__ (self,app):
    self.app = app
    app.title("Calculator")

    self.entry = Entry(app,width=30,borderwidth=5)
    self.entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

    # Buttons
    buttons = [
      ( ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("^", 4, 4),
        ("AC", 5, 0), ("sqrt", 5, 1), ("π", 5, 2), ("exp", 5, 3),)
    ]

    for (text, row, col) in buttons:
      b = tk.Button(app, text=text, width=5, height=2, command=lambda t=text: self.click(t))
      b.grid(row=row, column=col, padx=5, pady=5)

    self.mode = StringVar(value="basic")
    basic_button = Radiobutton(app,text="Basic",variable=self.mode,command=self.switch_mode)
    basic_button.grid(row=6,column=0,padx=5,pady=5)
    scientific_button = Radiobutton(app,text="Scientific",variable=self.mode,command=self.switch_mode)
    scientific_button.grid(row=6,column=1,padx=5,pady=5)

  def click(self,text):
    #create all the required trigonometric functions like sin, cos and so on
    #create buttons for all the functions and place them on the GUI and connect each function to the button
    #accept input using entry and pass to the functions according to the option chosen
    if text == "=":
      try:
        result = eval(self.entry.get())
        self.entry.delete(0,END)
        self.entry.insert(END,str(result))
      except:
        self.entry.delete(0,END)
        self.entry.insert(END,"Error")
    elif text == "AC":
      self.entry.delete(0,END)
    elif text == "sin":
      self.entry.insert(END,str(math.sin(float(self.entry.get()))))
    elif text == "cos":
      self.entry.insert(END,str(math.cos(float(self.entry.get()))))
    elif text == "tan":
      self.entry.insert(END,str(math.tan(float(self.entry.get()))))
    elif text == "^":
      self.entry.insert(END,"**")
    elif text == "sqrt":
      self.entry.insert(END,"math.sqrt(")
    elif text == "π":
      self.entry.insert(END,str(math.pi))
    elif text == "exp":
      self.entry.insert(END,"math.exp(")
    else:
      self.entry.insert(END,text)
    
  def switch_mode(self):
    mode = self.mode.get()
    if mode == "basic":
      self.app.geometry("300x300")
      self.entry.config(width=30)
    elif mode == "scientific":
      self.app.geometry("400x400")
      self.entry.config(width=40)

window = Tk()
calc = Calculator(window)
window.mainloop()

    


    



    

