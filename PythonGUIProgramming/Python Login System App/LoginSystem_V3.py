# Step 1: Import all the libraries
import tkinter as tk
from tkinter import messagebox

# Step 2: Create the main window and define it as a parent variable
parent = tk.Tk()
parent.title("Login System")

# Set the window size
window_width = 300
window_height = 200

# Get the screen width and height
screen_width = parent.winfo_screenwidth()
screen_height = parent.winfo_screenheight()

# Calculate the position (center the window)
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the geometry
parent.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Step 3: Create and place the username label and entry
username_label = tk.Label(parent, text="Username:", fg="blue")
username_label.pack()
username_entry = tk.Entry(parent, bg="lightgrey", fg="black")
username_entry.pack()

# Step 4: Create and place the password label and entry
password_label = tk.Label(parent, text="Password:", fg="blue")
password_label.pack()
password_entry = tk.Entry(parent, show="*", bg="lightgrey", fg="black")  # Show asterisks for the password
password_entry.pack()

# Step 6a: Function to validate login
def validate_login():
    # Step 6b: Add your own validation logic
    if username_entry.get() == "harshamalipeddi" and password_entry.get() == "H@rvi$ha211#":
        messagebox.showinfo("Login Successful", "Welcome, Harsha!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Step 5: Create and place the login button and define a function to validate the login
login_button = tk.Button(parent, text="Login", command=validate_login, bg="green", fg="white")
login_button.pack()

# Step 7: Start the tkinter window event loop
parent.mainloop()
