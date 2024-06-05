from tkinter import *

def calc_payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get():
        years = int(term_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        loan = float(amount_entry.get())
        
        monthly_rate = rate / 100 / 12
        
        # Calculating monthly payment (EMI)
        emi = (loan * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        emi_formatted = f"{emi:,.2f}"
        emi_label.config(text="EMI: ${}".format(emi_formatted))
        
        # Calculating total payment
        total_payment = emi * months
        total_payment_label.config(text="Total Payment: ${:,.2f}".format(total_payment))
        
        # Calculating simple interest
        simple_interest = (loan * rate * years) / 100
        simple_interest_label.config(text="Simple Interest: ${:.2f}".format(simple_interest))
        
    else:
        emi_label.config(text="")
        simple_interest_label.config(text="")
        total_payment_label.config(text="")

def clear():
    amount_entry.delete(0, END)
    interest_entry.delete(0, END)
    term_entry.delete(0, END)
    emi_label.config(text="")
    simple_interest_label.config(text="")
    total_payment_label.config(text="")

app = Tk()
app.title("Citibank - Mortgage Calculator")
app.geometry("600x600")
app.config(background="lightgray")

mortgage_logo = PhotoImage(file="assets\\mortgage_clipart.png")
citi_logo = PhotoImage(file="assets\\citi_logo.png")

app.iconphoto(True, citi_logo)

label_frame = LabelFrame(app, text="Mortgage Calculator")
label_frame.pack(pady=30)

mortgage_logo_label = Label(label_frame, image=mortgage_logo, text="Mortgage Calculator Application", compound="left")
mortgage_logo_label.grid(row=0, columnspan=2, pady=10)

frame = Frame(label_frame)
frame.grid(row=1, pady=20)

amount_label = Label(frame, text="Principal Amount ($)")
amount_entry = Entry(frame, font=("Helvetica", 30))

interest_label = Label(frame, text="Rate of Interest (%)")
interest_entry = Entry(frame, font=("Helvetica", 30))

term_label = Label(frame, text="Term (years)")
term_entry = Entry(frame, font=("Helvetica", 30))

amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

calculate_payment_button = Button(label_frame, text="Calculate Payment", command=calc_payment, bg="green")
calculate_payment_button.grid(row=2)

clear_button = Button(label_frame, text="Clear", command=clear, bg="red")
clear_button.grid(row=3)

emi_label = Label(label_frame, text="", font=("Helvetica", 20))
emi_label.grid(row=4, pady=5)

simple_interest_label = Label(label_frame, text="", font=("Helvetica", 20))
simple_interest_label.grid(row=5, pady=5)

total_payment_label = Label(label_frame, text="", font=("Helvetica", 20))
total_payment_label.grid(row=6, pady=5)

app.mainloop()
