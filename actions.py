# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart
from components import Store

site_name = "Shehab's Zone"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores:
        print('-' + store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store_name.lower() == store.name.lower():
            return store
    print("please choose a valid store")

def pick_store():
    """
    prompts user to pick a store.
    """
    user_picked = input("Pick a store!\n")
    right_store = get_store(user_picked)
    while not right_store:
        user_picked = input("")
        right_store = get_store(user_picked)
    return right_store


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    user_input = input("Choose a product\n")
    for item in picked_store.products:
        while user_input.lower() == item.name.lower():
            print("===========\nYou have chosen %s" % user_input)
            cart.add_to_cart(item)
            user_input = input('wana add more? Or Type checkout to checkout and proceed with the payment\n')
    if user_input == "checkout":
        cart.checkout()
    elif user_input != item.name.lower():
        print("Please choose a valid product!")
        pick_products(cart, picked_store)





def shop():
    """
    The main shopping functionality
    """
    print_stores()
    store = pick_store()
    cart = Cart()
    pick_products(cart, store)


def thank_you():
    print("                                  ==============")
    print("Thank you for shopping with us at %s" % site_name)
    print("                                  ==============")
