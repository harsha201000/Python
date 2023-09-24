from tkinter import *

# Loan Calculator Class
class LoanCalculator:
    def __init__(self):
        # Creae a GUI Window
        window = Tk()
        # Set the window size
        window.geometry("400x200")
        # Set the window title
        window.title("Loan Calculator")
        # Set the window background color
        window.config(background="lightgreen")
        # Create the input boxes
        ai_rate = Label(window, text="Annual Interest Rate",bg="red",fg="black")
        ai_rate.grid(row=1,column=1,sticky=W)
        
        no_of_years = Label(window, text="Number of Years",bg="red",fg="black")
        no_of_years.grid(row=2,column=1,sticky=W)
        
        loan_amount = Label(window, text="Loan Amount",bg="red",fg="black")
        loan_amount.grid(row=3,column=1,sticky=W)
        
        monthly_payment = Label(window, text="Monthly Payment",bg="red",fg="black")
        monthly_payment.grid(row=4,column=1,sticky=W)
        
        total_payment = Label(window, text="Total Payment",bg="red",fg="black")
        total_payment.grid(row=5,column=1,sticky=W)
        # Accept inputs
        self.aiRateVar = StringVar()
        
        self.aiRateEntry = Entry(window,textvariable=self.aiRateVar,justify=RIGHT,bg="lightgrey")
        self.aiRateEntry.grid(row=1,column=2)
        
        self.noOfYearsVar = StringVar()
        
        self.noOfYearsEntry = Entry(window,textvariable=self.noOfYearsVar,justify=RIGHT,bg="lightgrey")
        self.noOfYearsEntry.grid(row=2,column=2)
        
        self.loanAmtVar = StringVar()
        
        self.loanAmtEntry = Entry(window,textvariable=self.loanAmtVar,justify=RIGHT,bg="lightgrey")
        self.loanAmtEntry.grid(row=3,column=2)
        
        self.monthlyPaymentVar = StringVar()
        
        self.monthlyPaymentLabel = Label(window,textvariable=self.monthlyPaymentVar,justify=RIGHT,bg="gray")
        self.monthlyPaymentLabel.grid(row=4,column=2,sticky=E)
        
        self.totalPaymentVar = StringVar()
        
        self.totalPaymentLabel = Label(window,textvariable=self.totalPaymentVar,justify=RIGHT,bg="gray")
        self.totalPaymentLabel.grid(row=5,column=2,sticky=E)
        
        # Create a button
        ComputePaymentButton = Button(window,text="Compute Payment",command=self.compute_payment,bg="gray",fg="black",bd=10)
        ComputePaymentButton.grid(row=6,column=2,sticky=E)
        
        # Run the app
        window.mainloop()
        
    # Compute the total payment using compute_payment function
    def compute_payment(self):
        
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmtVar.get()),float(self.aiRateVar.get()) / 1200, int(self.noOfYearsVar.get()))
        
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.noOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment
        root = Tk()
        
    
    
LoanCalculator()