tips = [10, 12, 15]

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("What percentage tip would you like to leave? 10, 12, or 15?: "))
if tip in tips:
    total = bill + ((tip / 100) * bill)
    
share = total / people     

print(f"Each person should pay: ${share:.2f}")