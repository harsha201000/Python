import os

#Clear Screen
os.system("cls")

#Project title
print("Welcome to the ATM Bank in U.S")

#ATM Pin
atm_pin = int(input("Enter the 4 digit pin : "))
print(atm_pin)

#Create a variable called bank_balance
bank_balance = 1000

#Verify if atm pin is equal to 1981
if atm_pin == 1981:
    print("Enter 1 to withdraw amount")
    print("Enter 2 to deposit cash to your account")
    print("Enter 3 to check your balance")
    print("Enter 4 for fast cash withdrawl")
    choices = int(input("Please choose transactions : "))
    if choices == 1:
        withdraw_amount = int(input("Enter the withdraw amount : "))
        transactions = bank_balance - withdraw_amount
        print("Please collect your cash in $. {}".format(withdraw_amount))
        print("Thank you for choosing ATM Bank, your available balance is {}".format(transactions))
    elif choices == 2:
        deposit_amount = int(input("Enter the deposit amount : "))
        reflected_amt = bank_balance + deposit_amount
        print("The amount {} was successfully deposited into your bank account".format(deposit_amount))
        print("Thank you for choosing ATM Bank, your available balance is {}".format(reflected_amt))
    elif choices == 3:
        print("Your available bank balance is {}".format(bank_balance))
        print("Thank you for choosing ATM Bank")
    elif choices == 4:
        print("Your fast cash options are...")
        print("Enter 1 for 100")
        print("Enter 2 for 200")
        print("Enter 3 for 300")
        print("Enter 4 for 400")
        print("Enter 5 for 500")
        print("Enter 6 for 600")
        print("Enter 7 for 700")
        print("Enter 8 for 800")
        print("Enter 9 for 900")
        print("Enter 10 for 1000")
        fast_cash_code = int(input("Enter the ammount code: "))
        if fast_cash_code == 1 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 100)
        elif fast_cash_code == 2 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 200)
        elif fast_cash_code == 3 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 300)
        elif fast_cash_code == 4 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 400)
        elif fast_cash_code == 5 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 500)
        elif fast_cash_code == 6 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 600)
        elif fast_cash_code == 7 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 700)
        elif fast_cash_code == 8 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 800)
        elif fast_cash_code == 9 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 900)
        elif fast_cash_code == 10 :
            print("Thank you for choosing ATM Bank. Total balance " ,bank_balance - 1000)
        else:
            print("wrong choice")
else:
    print("ATM pin is wrong, Please Try again!")
    