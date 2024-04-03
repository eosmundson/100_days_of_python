# Enter your height in meters e.g, 1.55
height = float(input("Enter your height in meters: "))
# Enter your weight in kilograms e.g, 72
weight = int(input("Enter your weight in kg: "))

bmi = weight / (height * height)

print(f"Your BMI is {bmi:.2f}.")