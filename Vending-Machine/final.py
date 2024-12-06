import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class Store:
    def __init__(self):
        self.revenue = 0
        self.purchase_history = []
        self.customer_points = {}

    def add_purchase(self, items, total_cost, phone_number):
        self.purchase_history.append({'phone_number': phone_number, 'items': items, 'cost': total_cost})
        self.revenue += total_cost

        if phone_number not in self.customer_points:
            self.customer_points[phone_number] = 0
        self.customer_points[phone_number] += total_cost // 10

class VendingMachine:
    def __init__(self, root, store):
        self.root = root
        self.store = store
        self.root.title("Vending Machine")
        self.root.geometry("900x750")
        self.root.config(bg="#f0f0f0")

        self.items = {
            "Drinks": {
                "Water": {"price": 10, "image": "water.jpg"},
                "Coca-Cola": {"price": 15, "image": "cola.jpg"},
                "Pepsi": {"price": 15, "image": "pepsi.png"},
                "Fanta": {"price": 15, "image": "fanta.jpg"}
            },
            "Snacks": {
                "Chips": {"price": 20, "image": "chips.jpg"},
                "Chocolate": {"price": 25, "image": "choc.jpg"},
                "Biskit": {"price": 40, "image": "biskit.jpg"}
            },
            "Foods": {
                "Burger": {"price": 39, "image": "burger.jpg"},
                "Sausage": {"price": 42, "image": "sausage.jpg"}
            }
        }
        self.balance = 0
        self.selections = []
        self.current_category = "Drinks"

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Welcome to the Vending Machine!", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=15)

        category_frame = tk.Frame(self.root, bg="#f0f0f0")
        category_frame.pack(pady=10)
        tk.Label(category_frame, text="Select Category:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333").pack(side=tk.LEFT, padx=5)
        
        self.category_var = tk.StringVar(value="Drinks")
        category_dropdown = tk.OptionMenu(category_frame, self.category_var, *self.items.keys(), command=self.update_item_display)
        category_dropdown.config(font=("Helvetica", 12), bg="#ffffff")
        category_dropdown.pack(side=tk.LEFT, padx=5)

        self.item_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.item_frame.pack(pady=10)
        self.update_item_display("Drinks")

        self.selection_label = tk.Label(self.root, text="Selected: None", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
        self.selection_label.pack(pady=10)

        self.balance_label = tk.Label(self.root, text="Balance: 0 THB", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
        self.balance_label.pack(pady=10)

        payment_frame = tk.Frame(self.root, bg="#f0f0f0")
        payment_frame.pack(pady=10)

        self.money_input = tk.Entry(payment_frame, font=("Helvetica", 12), width=15)
        self.money_input.grid(row=0, column=0, padx=5)

        insert_button = tk.Button(payment_frame, text="Insert Money", command=self.insert_money, font=("Helvetica", 12), bg="#B2BEBF", fg="white", activebackground="#e68900", padx=10, pady=5)
        insert_button.grid(row=0, column=1, padx=5)

        purchase_button = tk.Button(self.root, text="Purchase", command=self.purchase_items, font=("Helvetica", 14, "bold"), bg="#889C9B", fg="white", activebackground="#1976D2", padx=10, pady=10)
        purchase_button.pack(pady=15)

        purchase_coupon_button = tk.Button(self.root, text="Purchase with Coupon", command=self.purchase_with_coupon, font=("Helvetica", 14, "bold"), bg="#486966", fg="white", activebackground="#FFB300", padx=10, pady=10)
        purchase_coupon_button.pack(pady=5)

        coupon_label = tk.Label(self.root, text="Every 10 points can be used to get a 20% discount.", font=("Helvetica", 10, "bold"), bg="#f0f0f0", fg="#333")
        coupon_label.pack(pady=5)

        bottom_frame = tk.Frame(self.root, bg="#f0f0f0")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10, anchor='se')

        exit_button = tk.Button(bottom_frame, text="Exit", command=self.root.quit, font=("Helvetica", 12), bg="#f44336", fg="white", activebackground="#d32f2f", padx=10, pady=5)
        exit_button.pack(side=tk.RIGHT, padx=5)
        
        admin_button = tk.Button(bottom_frame, text="Admin: Show Revenue", command=self.show_revenue, font=("Helvetica", 12), activebackground="#7B1FA2", padx=10, pady=5)
        admin_button.pack(side=tk.RIGHT, padx=5) 
        
        points_button = tk.Button(bottom_frame, text="Check Points", command=self.check_points_popup, font=("Helvetica", 12), activebackground="#689F38", padx=10, pady=5)
        points_button.pack(side=tk.RIGHT, padx=5)

    def update_item_display(self, category):
        self.current_category = category
        for widget in self.item_frame.winfo_children():
            widget.destroy()

        for item, details in self.items[category].items():
            item_frame = tk.Frame(self.item_frame, bd=2, relief="groove", bg="#ffffff")
            item_frame.pack(side=tk.LEFT, padx=15, pady=10)

            image = Image.open(details['image'])
            image = image.resize((120, 120))
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(item_frame, image=photo, bg="#ffffff")
            img_label.image = photo
            img_label.pack()

            button = tk.Button(item_frame, text=f"{item} - {details['price']} THB", command=lambda i=item: self.select_item(i),
                               font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45a049", padx=10, pady=5)
            button.pack(pady=5)

    def select_item(self, item):
        self.selections.append(item)
        self.selection_label.config(text=f"Selected: {', '.join(self.selections)}")

    def insert_money(self):
        try:
            amount = int(self.money_input.get())
            self.balance += amount
            self.balance_label.config(text=f"Balance: {self.balance} THB")
            self.money_input.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def purchase_items(self):
        if not self.selections:
            messagebox.showwarning("Warning", "No items selected.")
            return

        total_cost = sum(self.items[self.current_category][item]["price"] for item in self.selections)

        if self.balance < total_cost:
            messagebox.showwarning("Warning", "Insufficient balance.")
        else:
            self.balance -= total_cost
            change = self.balance

            phone_number = simpledialog.askstring("Enter Phone Number", "Enter your phone number to collect points:")
            if phone_number:
                self.store.add_purchase(self.selections, total_cost, phone_number)
                points = self.store.customer_points.get(phone_number, 0)
                messagebox.showinfo("Success", f"Purchased items. Change: {change} THB. Points: {points}")
            else:
                self.store.revenue += total_cost
                self.store.purchase_history.append({'phone_number': 'No points collected', 'items': self.selections, 'cost': total_cost})
                messagebox.showinfo("Purchase Complete", f"Purchased items. Change: {change} THB")

            self.balance = 0 
            self.reset()

    def purchase_with_coupon(self):
        if not self.selections:
            messagebox.showwarning("Warning", "No items selected.")
            return
        
        phone_number = simpledialog.askstring("Enter Phone Number", "Enter your phone number:")
        if not phone_number:
            return

        points = self.store.customer_points.get(phone_number, 0)
        if points < 10:
            messagebox.showwarning("Warning", "Not enough points to redeem a coupon.")
            return

        total_cost = sum(self.items[self.current_category][item]["price"] for item in self.selections)
        discount = total_cost * 0.2
        final_cost = total_cost - discount

        if self.balance < final_cost:
            messagebox.showwarning("Warning", "Insufficient balance after coupon.")
        else:
            self.balance -= final_cost
            self.store.customer_points[phone_number] -= 10 
            change = self.balance
            
            self.store.add_purchase(self.selections, final_cost, phone_number)
            messagebox.showinfo("Success", f"Purchased items with coupon. Change: {change} THB. Points left: {self.store.customer_points[phone_number]}")
            
            self.balance = 0 
            self.reset()

    def check_points_popup(self):
        phone_number = simpledialog.askstring("Check Points", "Enter your phone number:")
        if phone_number in self.store.customer_points:
            points = self.store.customer_points[phone_number]
            messagebox.showinfo("Customer Points", f"Earn 1 point for every 10 THB spent\nPhone: {phone_number}, Points: {points}")
        else:
            messagebox.showinfo("Customer Points", "No points for this customer.")
    
    def show_revenue(self):
        revenue_info = f"Total Revenue: {self.store.revenue} THB\nPurchase History:\n"
        for entry in self.store.purchase_history:
            revenue_info += f"Phone: {entry['phone_number']}, Items: {', '.join(entry['items'])}, Cost: {entry['cost']} THB\n"
        messagebox.showinfo("Store Revenue", revenue_info)

    def reset(self):
        self.selections = []
        self.selection_label.config(text="Selected: None")
        self.balance_label.config(text="Balance: 0 THB")

if __name__ == "__main__":
    store = Store()
    root = tk.Tk()
    vending_machine = VendingMachine(root, store)
    root.mainloop()
