import tkinter as tk

class RestaurantManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Management System")
        
        self.menu_file = "menu.txt"
        self.menu = {}
        self.load_menu_from_file()  # Load menu from file when the app starts

        self.menu_label = tk.Label(master, text="Menu")
        self.menu_label.grid(row=0, column=0, columnspan=2)

        self.menu_text = tk.Text(master, height=10, width=40)
        self.menu_text.grid(row=1, column=0, columnspan=2)

        self.add_label = tk.Label(master, text="Add New Dish")
        self.add_label.grid(row=2, column=0, columnspan=2)

        self.dish_label = tk.Label(master, text="Dish Name:")
        self.dish_label.grid(row=3, column=0)
        self.dish_entry = tk.Entry(master)
        self.dish_entry.grid(row=3, column=1)

        self.price_label = tk.Label(master, text="Price:")
        self.price_label.grid(row=4, column=0)
        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=4, column=1)

        self.add_button = tk.Button(master, text="Add Dish", command=self.add_dish)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.save_button = tk.Button(master, text="Save Menu", command=self.save_menu_to_file)
        self.save_button.grid(row=6, column=0, columnspan=2)

        self.update_menu_display()

    def add_dish(self):
        dish_name = self.dish_entry.get()
        price = self.price_entry.get()

        if dish_name and price:
            self.menu[dish_name] = float(price)
            self.update_menu_display()
            self.dish_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            print("Please enter both dish name and price.")

    def update_menu_display(self):
        self.menu_text.delete(1.0, tk.END)
        for dish, price in self.menu.items():
            self.menu_text.insert(tk.END, f"{dish}: ${price}\n")

    def save_menu_to_file(self):
        with open(self.menu_file, "w") as file:
            for dish, price in self.menu.items():
                file.write(f"{dish},{price}\n")
        print("Menu saved to file.")

    def load_menu_from_file(self):
        try:
            with open(self.menu_file, "r") as file:
                for line in file:
                    dish, price = line.strip().split(',')
                    self.menu[dish] = float(price)
        except FileNotFoundError:
            print("Menu file not found.")

def main():
    root = tk.Tk()
    app = RestaurantManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
