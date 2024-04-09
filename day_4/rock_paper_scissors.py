import random

player_choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))

rps_dict = {0 : "Rock", 1 : "Paper", 2 : "Scissors"}

computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 0:
    print(f"You both picked {rps_dict[0]}. It's a draw.")
if player_choice == 0 and computer_choice == 1:
    print(f"You picked {rps_dict[0]} and the computer picked {rps_dict[1]}. You lose.")
if player_choice == 0 and computer_choice == 2:
    print(f"You picked {rps_dict[0]} and the computer picked {rps_dict[2]}. You win.")
if player_choice == 1 and computer_choice == 0:
    print(f"You picked {rps_dict[1]} and the computer picked {rps_dict[0]}. You win.")
if player_choice == 1 and computer_choice == 1:
    print(f"You both picked {rps_dict[1]}. It's a draw.")
if player_choice == 1 and computer_choice == 2:
    print(f"You picked {rps_dict[1]} and the computer picked {rps_dict[2]}. You lose.")
if player_choice == 2 and computer_choice == 0:
    print(f"You picked {rps_dict[2]} and the computer picked {rps_dict[0]}. You lose.")
if player_choice == 2 and computer_choice == 1:
   print(f"You picked {rps_dict[2]} and the computer picked {rps_dict[1]}. You win.")
if player_choice == 1 and computer_choice == 2:
    print(f"You both picked {rps_dict[2]}. It's a draw.")