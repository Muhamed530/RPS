
# RPS

# initialize a list of rock, paper, and scissors to iterate through

# ask the user to choose an option

# iterate through list 

# pick a random option for the computer

#compare the two
import random

rps = ["rock","paper","scissors"]
user_counter = 0
i = 7
while i > 0 or user_counter == 4:
  user_choice = input('Choose (rock/paper/scissors): ')
  comp_choice = random.choice(rps)
  print("computer chose: " + comp_choice)
  print(user_choice + " vs " + comp_choice)
  if  comp_choice == user_choice.lower():
    print('Tie!')
    i += 1
  
  elif (user_choice == "rock" and comp_choice == "scissors") or (user_choice == "scissors" and comp_choice == "paper") or (user_choice == "paper" and comp_choice == "rock"):
    print("Win!")
    user_counter += 1
    
  
  elif user_choice not in rps:
    print('Must be rock, paper, or scissors!')
    i += 1

  else:
    print("LOSER!!!")

  i -= 1
  print('User Wins: ' + str(user_counter))

