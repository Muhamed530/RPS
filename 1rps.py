#Rock-Paper-Scissors


import random


tie = 0
computerWins = 0
userWins = 0
rps = ["rock", "paper", "scissors"]
round = 0

while userWins < 3 and computerWins < 3:
    user_input = input("Pick 1: rock, paper, or scissors: ")
    computers_choice = (random.choice(rps))
    print("User choice: " + user_input + "!")
    print("Computers Choice: " + computers_choice + "!")

    if user_input == computers_choice:
        print("Tie!")

    elif (user_input == "rock" and computers_choice == "scissors") or \
        (user_input == "paper" and computers_choice == "rock") or \
        (user_input == "scissors" and computers_choice == "paper"):
        userWins += 1
        print("You Win!")
    elif (user_input == "rock" and computers_choice == "paper") or \
        (user_input == "paper" and computers_choice == "scissors") or \
        (user_input == "scissors" and computers_choice == "rock"):
        computerWins += 1
        print("Computer Wins!")
    else:
        print("Error!!!")
    round += 1
print("User won", userWins, "times out of", round, "rounds!!!!!")
print("Computer won", computerWins, "times out of", round, "rounds!!!!!")