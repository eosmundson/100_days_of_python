print("The Lova Calculator is calulating your score...")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

# Count number of occurrences of letters
count1 = 0
count2 = 0
names = name1.lower() + name2.lower()
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
for _ in true:
    for i in names:
        if i == _:
            count1 += 1
for _ in love:
    for i in names:
        if i == _:
            count2 += 1

score = int(str(count1) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")