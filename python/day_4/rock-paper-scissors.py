import random

# Rock
rock = ''' ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = ''' PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = ''' SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play Rock Paper Scissors!")
choices = [0,1,2]
hand = [rock, paper, scissors]

map = [choices, hand]
hand_row = 1

player_choice = int(input("Choose: (0) Rock, (1) Paper, (2) Scissors: "))
computer_choice = random.randint(0,2)

print(f"You chose: {map[hand_row][player_choice]}\n")
print(f"Computer chose: {map[hand_row][computer_choice]}")


if computer_choice == player_choice:
    print("TIE")
    exit(0)
else:
    if (computer_choice == choices[0] and player_choice == 1) or (computer_choice == choices[1] and player_choice == choices[2]) or (computer_choice == choices[2] and player_choice == choices[0]):
        print("YOU WIN")
    else:
        print("YOU LOSE")