class Ecommerce:
    def __init__(self, product=None, quantity=0, price=0, discount=0):
        self.__product = product
        self.__quantity = quantity
        self.__price = price
        self.__discount = discount
    # Getter Methods
    def get_product(self):
        return self.__product
    def get_quantity(self):
        return self.__quantity
    def get_price(self):
        return self.__price
    def get_discount(self):
        return self.__discount
    # Setter Methods
    def set_product(self, product):
        self.__product = product
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def set_price(self, price):
        self.__price = price
    def set_discount(self, discount):
        self.__discount = discount
    # Add Product
    def add_product(self):
        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        discount = float(input("Enter Discount %: "))
        ecommerce_obj = Ecommerce(product, quantity, price, discount)
        product_data.append(ecommerce_obj)
        print("Product Added Successfully!")
    # View Products
    def view_products(self):
        if len(product_data) == 0:
            print("No Products Available")
            return
        print("\n PRODUCT LIST")
        for data in product_data:
            print(
                "Product:", data.get_product(),
                "\nQuantity:", data.get_quantity(),
                "\nPrice:", data.get_price(),
                "\nDiscount:", data.get_discount(),
                "\n----------------------"
            )
    # Update Quantity
    def update_quantity(self):
        product = input("Enter Product Name: ")
        for data in product_data:
            if data.get_product() == product:
                new_quantity = int(input("Enter New Quantity: "))
                data.set_quantity(new_quantity)
                print("Quantity Updated Successfully!")
                return
        print("Product Not Found!")
    # Remove Product
    def remove_product(self):
        product = input("Enter Product Name: ")
        for data in product_data:
            if data.get_product() == product:
                product_data.remove(data)
                print("Product Removed Successfully!")
                return
        print("Product Not Found!")
    # Generate Bill
    def generate_bill(self):

        if len(product_data) == 0:
            print("No Products Available")
            return

        total_bill = 0

        print("\n========== BILL ==========")

        for data in product_data:
            quantity = data.get_quantity()
            price = data.get_price()
            discount = data.get_discount()
            subtotal = quantity * price
            discount_amount = subtotal * (discount / 100)
            final_amount = subtotal - discount_amount
            total_bill += final_amount
            print(
                f"Product: {data.get_product()}\n"
                f"Quantity: {quantity}\n"
                f"Price: ₹{price}\n"
                f"Subtotal: ₹{subtotal}\n"
                f"Discount: {discount}%\n"
                f"Final Amount: ₹{final_amount}\n"
            )
        print("TOTAL BILL = ₹", total_bill)
# Main Program
if __name__ == '__main__':
    print("WELCOME TO E-COMMERCE SYSTEM")
    product_data = []
    ecommerce = Ecommerce()
    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Update Quantity")
        print("4. Remove Product")
        print("5. Generate Bill")
        print("6. Exit")
        option = int(input("Please Select Option: "))
        if option == 1:
            ecommerce.add_product()
        elif option == 2:
            ecommerce.view_products()
        elif option == 3:
            ecommerce.update_quantity()
        elif option == 4:
            ecommerce.remove_product()
        elif option == 5:
            ecommerce.generate_bill()
        elif option == 6:
            print("Thank You!")
            break
        else:
            print("Please Select Valid Option")