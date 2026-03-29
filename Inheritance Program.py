
class Inventory:


         def __init__(self, item, price, discount):
             self.item = item
             self.price = int(price)
             self.discount = float(discount)

         def price_for(self, quantity):
             return self.price * quantity

         def discount_for(self, quantity):
             total = self.price_for(quantity)
             if self.discount > 0:
                 total -= total * self.discount
             return total


class Sugar(Inventory):
         def __init__(self):
             super().__init__("Sugar", 2, .10)

class Milk(Inventory):
         def __init__(self):
             super().__init__("Milk",2,0)

class Eggs(Inventory):
         def __init__(self):
             super().__init__("Eggs",4,.20)

class Flour(Inventory):
         def __init__(self):
             super().__init__("Flour", 3, .10)

class Chicken(Inventory):
         def __init__(self):
             super().__init__("Chicken", 12,.30)

class Fish(Inventory):
         def __init__(self):
             super().__init__("Fish", 11,0)


print("Hello welcome into Lows supermarket, we sell sugar,milk,eggs,flour,chicken and fish")
print("Deals of the Day:")
print("10% off all sugar and flour")
print("20% off eggs")
print("30% off chicken")

cart = []
subtotal = 0

while True:

    items = input("Please enter what you want to put in your shopping cart:").lower()

    print(f"how many {items} would you like to put in your shopping cart?")
    qty = int(input())

    if items == "sugar":
        item = Sugar()

    elif items == "milk":
        item = Milk()

    elif items == "eggs":
        item = Eggs()

    elif items == "flour":
        item = Flour()

    elif items == "chicken":
        item = Chicken()

    elif items == "fish":
        item = Fish()
    else:
        print("We dont offer that item here ")
        continue
    cart.append((item, qty))

    print("Would you like to do more shopping?")
    print("Enter 'yes' or 'no': ")
    shoppingcart = input().lower()
    if shoppingcart == "yes":
        pass

    else:
        break


print("\n----- RECEIPT -----")
grand_total = 0

for item, qty in cart:
    line_total = item.price_for(qty)
    discount_total = item.discount_for(qty)
    grand_total += discount_total
    subtotal += line_total

    print(f"{qty} x {item.item}             ${line_total}")
    print(f"${item.price} for each")


print("")

print(f"Subtotal: {subtotal}")
if item.discount > 0:
    print(f"Discount applied: {int(item.discount*100)}%")
print(f"Grand total: {grand_total}")



