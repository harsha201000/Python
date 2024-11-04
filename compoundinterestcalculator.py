from tkinter import *


def clear():
  principal_field.delete(0, END)
  rate_field.delete(0, END)
  time_field.delete(0, END)
  compound_field.delete(0, END)

  principal_field.focus_set()


def calculate_ci():
  principal = int(principal_field.get())
  rate = float(rate_field.get())
  time = int(time_field.get())

  CI = principal * (pow((1 + rate / 100), time))

  compound_field.insert(10, CI)
  


app = Tk()
app.geometry("400x250")
app.title("Compound Interest Calculator")


app.configure(background="lightgreen")

principal_amount = Label(app, text="Principal Amount (Rs.) : ", fg='black', background='red')
rate_amount = Label(app, text="Rate(%) : ", fg='black', background='red')
time_amount = Label(app, text="Time(years) : ", fg='black', background='red')
compound_interest = Label(app, text="Compound Interest : ", fg='black', background='red')

principal_field = Entry(app)
rate_field = Entry(app)
time_field = Entry(app)
compound_field = Entry(app)


principal_amount.grid(row=1, column=0, padx=10, pady=10)
rate_amount.grid(row=2, column=0, padx=10, pady=10)
time_amount.grid(row=3, column=0, padx=10, pady=10)
compound_interest.grid(row=5, column=0, padx=10, pady=10)

principal_field.grid(row=1, column=1, padx=10, pady=10)
rate_field.grid(row=2, column=1, padx=10, pady=10)
time_field.grid(row=3, column=1, padx=10, pady=10)
compound_field.grid(row=5, column=1, padx=10, pady=10)

calculate_btn = Button(app, text="Calculate", bg="grey", foreground="black", command=calculate_ci)
clear_btn = Button(app, text="Clear", bg="grey", foreground="black", command=clear)

calculate_btn.grid(row=4, column=1, pady=10)
clear_btn.grid(row=6, column=1, pady=10)

app.mainloop()