import random


names = "Angela, Ben, Jenny, Michael, Chloe".split(", ")

pick = random.randint(0,4)

print(f"{names[pick]} is going to buy the meal today!")