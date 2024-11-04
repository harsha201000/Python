import tkinter as tk
from tkinter import messagebox

# Function to get the selected contact
def get_selected_contact():
    selected_item = contact_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        contact = contacts[index]
        messagebox.showinfo("Selected Contact", f"Name: {contact['name']}\nNumber: {contact['number']}")

# Function to add a contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contact = {'name': name, 'number': number}
        contacts.append(contact)
        contact_listbox.insert(tk.END, name)
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Both Name and Number fields are required.")

# Function to edit a contact
def edit_contact():
    selected_item = contact_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        name = name_entry.get()
        number = number_entry.get()
        if name and number:
            contact = contacts[index]
            contact['name'] = name
            contact['number'] = number
            contact_listbox.delete(index)
            contact_listbox.insert(index, name)
            name_entry.delete(0, tk.END)
            number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both Name and Number fields are required.")

# Function to view a contact
def view_contact():
    selected_item = contact_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        contact = contacts[index]
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
        name_entry.insert(0, contact['name'])
        number_entry.insert(0, contact['number'])

# Function to exit the app
def exit_app():
    window.destroy()

# Function to reset name and number fields
def reset_fields():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

contacts = []

window = tk.Tk()
window.title("Address/Contact Book")

# Create and configure listbox
contact_listbox = tk.Listbox(window)
contact_listbox.pack()

# Create labels and entry widgets for name and number
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

number_label = tk.Label(window, text="Number:")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()

# Create buttons
get_button = tk.Button(window, text="Get Selected Contact", command=get_selected_contact)
get_button.pack()

add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack()

edit_button = tk.Button(window, text="Edit Contact", command=edit_contact)
edit_button.pack()

view_button = tk.Button(window, text="View Contact", command=view_contact)
view_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack()

reset_button = tk.Button(window, text="Reset Fields", command=reset_fields)
reset_button.pack()

window.mainloop()