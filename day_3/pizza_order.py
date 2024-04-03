print("Thank you for choosing Python Pizza Delivery!")
size = input("What size pizza would you like? S, M, or L?: ")
add_pepperoni = input("Would you like pepperoni?: ")
extra_cheese = input("Would you like extra cheese?: ")

if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25

if add_pepperoni == "Y" and size == "S":
    price = price + 2
elif add_pepperoni == "Y" and size == "M" or add_pepperoni == "Y" and size == "L":
    price = price + 3
    
if extra_cheese == "Y":
    price = price + 1

print(f"Your {size} pizza costs ${price}.")
