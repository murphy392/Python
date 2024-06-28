import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('Do you want rock, paper, or scissors?\n')

print('Computer choice: ', computer_choice)

if computer_choice == user_choice:
  print('Tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
  print('Win!')
elif user_choice == 'paper' and computer_choice == 'rock':
  print('Win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
  print('Win!')
else:
  print('You lose, computer wins!')

