# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: ___Jessica____
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: ____________Hamburgers____________
# ============================================================

# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Burgers:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 0:
            print("no.")
        else:
            self.price = price

    def deliver(self):
        print(f"Delivering your {self.name}!")

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: it will print "no." because the price is below zero.
#   Paste the message you see here: _no.__



# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class Fries(Burgers):
    def deliver(self):
        print(f"Delivering your {self.name} with ketchup!")

burger = Burgers("Cheeseburger", 3.50)
fries = Fries("Fries", 2.50)

burger.deliver()
fries.deliver()


# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: __cheeseburger___

item1 = Burgers("cheeseburger", 3.50)
item2 = Burgers("hamburger", 3.00)
item3 = Burgers("veggieburger", 4.00)
item4 = Fries("fries", 2.50)
print(item1.name)
print(item2.name)
print(item3.name)
print(item4.name)
print(item1.price)
print(item2.price)
print(item3.price)
print(item4.price)
print(item1.deliver())
print(item2.deliver())
print(item3.deliver())
print(item4.deliver())
print(total := item1.price + item2.price + item3.price + item4.price)




# PREDICT : This will print the names of the items: cheeseburger, hamburger, veggieburger

# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
        print(f"Added {item.name} to cart.")
    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total += item.price
        print(f"Total: ${total:.2f}")

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {
    "1": item1,
    "2": item2,
    "3": item3,
    "4": item4,
    "cart": Cart()
}

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________
while True:
    choice = input("Pick an item (1, 2, 3, or 4), or 'done' to finish: ")
    if choice == "done":
        break
    else:
        store["cart"].add(store[choice])

store["cart"].checkout()

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
print("Checking out...")
print("Delivering items:")
store["cart"].checkout()


# I predict that the output will show the items being delivered and the total price at the end.

# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
