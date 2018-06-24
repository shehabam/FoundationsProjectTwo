# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.product = product
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for product in self.products:
            print('- Name: %s\n- Descripton: %s\n- Price: %s KD\n================' % (self.product.name, self.product.description, self.product.price))


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price
# TODO: CHECK THIS SOLUTION DOWN HERE __STR__()
    def __str__(self):
        # for product in self.products:
        #     return product
        return (self.name + " " + self.description + " %s" % self.price)

class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.cart_products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.product = product
        self.cart_products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for product in self.cart_products:
            total += product.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        for product in self.cart_products:
            print('- ' + product.name)
        print("Your price is: " + str(self.get_total_price()) + ' KD')


    def checkout(self):
        """
        Does the checkout.
        """
        print("you are about to checkout, your order is: ")
        self.print_receipt()
        user_input = input("Type y to confirm or, n to cancel\n")
        if user_input == "y":
            print("Your order has been placed. Please come take your order we don't work for you!")
        else:
            print("Your order has been cancelled. matshof shr")
