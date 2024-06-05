# Codeyoung Python Level 1 - Class 47 & 48 Final Project

# Import modules
from tkinter import *
import datetime

# Functions for submit and clear buttons
def submit():
    listbox.insert(1, order_no_entry.get())
    listbox.insert(2, fries_meal_entry.get())
    listbox.insert(3, lunch_meal_entry.get())
    listbox.insert(4, burger_meal_entry.get())
    listbox.insert(5, pizza_meal_entry.get())
    listbox.insert(6, cheese_burger_entry.get())
    listbox.insert(7, drinks_entry.get())   

def clear():
    listbox.grid(row=11,column=1)
    listbox.delete(0,END)
    order_no_entry.delete(0,END)
    fries_meal_entry.delete(0,END)
    lunch_meal_entry.delete(0,END)
    burger_meal_entry.delete(0,END)
    pizza_meal_entry.delete(0,END)
    cheese_burger_entry.delete(0,END)
    drinks_entry.delete(0,END)
    
# Creating the Window and adding the name and setting size
window = Tk()
window.title("Restarunt Management System")
window.geometry("500x500")

# Adding Background color to window
window.config(bg="darkgrey")

# Adding an iconphoto to the window
logo = PhotoImage(file="appicon.png")
window.iconphoto(True,logo)

# Creating an order summary label 
ordersummarylabel = Label(window,text="Order Summary Label: ", fg="black", bg="darkgrey")
ordersummarylabel.grid(row=11,column=0)

# Creating a listbox to to see how many meals you ordered
listbox = Listbox(window, height=10, width=20, bg="white")
listbox.grid(row=11,column=1)

# App Header
header = Label(window, text="Restarunt Management System", fg="black", font=("Arial", 12, "bold"), bg="yellow")
header.grid(row=0,column=1)

# Setting Current Datetime
current_datetime = datetime.datetime.now()

# Adding Datetime label to display current date and time
datetime_label = Label(window, text=current_datetime, fg="lightgreen", bg="black")
datetime_label.grid(row=1,column=1)

# Create a order number label
order_no_label = Label(window, text="Order No.", fg="black", bg="lightgreen")
order_no_label.grid(row=2,column=0)

# Create a order number entry to enter the order number
order_no_entry = Entry(window, bg="lightblue")
order_no_entry.grid(row=2,column=1)

# Create a fries meal label
fries_meal_label = Label(window, text="Fries Meal", fg="black", bg="lightgreen")
fries_meal_label.grid(row=3,column=0)

# Create a fries meal entry to enter how many fries you want
fries_meal_entry = Entry(window, bg="lightblue")
fries_meal_entry.grid(row=3,column=1)

# Create a lunch meal label
lunch_meal_label = Label(window, text="Lunch Meal", fg="black", bg="lightgreen")
lunch_meal_label.grid(row=4,column=0)

# Create a lunch meal entry to enter how many lunch meals you want
lunch_meal_entry = Entry(window, bg="lightblue")
lunch_meal_entry.grid(row=4,column=1)

# Create a burger meal label
burger_meal_label = Label(window, text="Burger Meal", fg="black", bg="lightgreen")
burger_meal_label.grid(row=5,column=0)

# Create a burger meal entry to enter how many burger meals you want
burger_meal_entry = Entry(window, bg="lightblue")
burger_meal_entry.grid(row=5,column=1)

# Create a pizza meal label
pizza_meal_label = Label(window, text="Pizza Meal", fg="black", bg="lightgreen")
pizza_meal_label.grid(row=6,column=0)

# Create a pizza meal entry to enter how many pizzas meals you want
pizza_meal_entry = Entry(window, bg="lightblue")
pizza_meal_entry.grid(row=6,column=1)

# Create a cheese burger label
cheese_burger_label = Label(window, text="Cheese burger", fg="black", bg="lightgreen")
cheese_burger_label.grid(row=7,column=0)

# Create a cheese burger entry to enter how many cheeseburgers meals you want
cheese_burger_entry = Entry(window, bg="lightblue")
cheese_burger_entry.grid(row=7,column=1)

# Create a drinks label
drinks_label = Label(window, text="Drinks", fg="black", bg="lightgreen")
drinks_label.grid(row=8,column=0)

# Create a drinks entry to enter how many drinks you want
drinks_entry = Entry(window, bg="lightblue")
drinks_entry.grid(row=8,column=1)

# Add a submit button to submit the quantity of your meals
submit_button = Button(window, text="Submit", fg="black", bg="green", command=submit)
submit_button.grid(row=10,column=1)

# Add a clear button to clear everything
clear_button = Button(window, text="Clear", fg="black", bg="red", command=clear)
clear_button.grid(row=10,column=0)

# Add a event loop for thw window
window.mainloop()