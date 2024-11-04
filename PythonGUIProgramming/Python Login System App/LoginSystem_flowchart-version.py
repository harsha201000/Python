# Step 1: Import all the libraries
import tkinter as tk
from tkinter import messagebox

# Step 2: Create the main window and define it as a parent variable
parent = tk.Tk()
parent.title("Login System")

# Step 3: Create and place the username label and entry
username_label = tk.Label(parent, text="Username:")
username_label.pack()
username_entry = tk.Entry(parent)
username_entry.pack()

# Step 4: Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()
password_entry = tk.Entry(parent, show="*")  # Show asterisks for the password
password_entry.pack()

# Step 6a: Function to validate login
def validate_login():
    # Step 6b: Add your own validation logic
    if username_entry.get() == "admin" and password_entry.get() == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Step 5: Create and place the login button and define a function to validate the login
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Step 7: Start the tkinter window event loop
parent.mainloop()
