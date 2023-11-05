from tkinter import * 
from tkinter import messagebox

class ShoppingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Shopping App")
        
        # Initialize products
        self.products = [
            {"name": "Product 1", "price": 10.0},
            {"name": "Product 2", "price": 20.0},
            {"name": "Product 3", "price": 30.0},
        ]
        
        self.cart = []

        # Create a label for the title
        title_label = Label(window, text="Welcome to Shopping App", font=("Helvetica", 16))
        title_label.pack()

        # Create a listbox to display products
        self.product_listbox = Listbox(window)
        self.product_listbox.pack()

        # Add products to the listbox
        for product in self.products:
            self.product_listbox.insert(END, f"{product['name']} - ${product['price']:.2f}")

        # Create an "Add to Cart" button
        add_to_cart_button = Button(window, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack()

        # Create a listbox to display the cart
        self.cart_listbox = Listbox(window)
        self.cart_listbox.pack()

        # Create a "Checkout" button
        checkout_button = Button(window, text="Checkout", command=self.checkout)
        checkout_button.pack()

    def add_to_cart(self):
        selected_product = self.product_listbox.get(ACTIVE)
        product_name = selected_product.split(" - ")[0]
        
        for product in self.products:
            if product['name'] == product_name:
                self.cart.append(product)
                self.cart_listbox.insert(END, f"{product['name']} - ${product['price']:.2f}")

    def checkout(self):
        total_price = sum(product['price'] for product in self.cart)
        messagebox.showinfo("Checkout", f"Total Price: ${total_price:.2f}")

if __name__ == "__main__":
    window = Tk()
    app = ShoppingApp(window)
    window.mainloop()