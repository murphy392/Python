import random
roll = random.randint(1,6)

guess = int(input('Guess the dice roll: \n'))

if guess == roll:
  print("correct! They rolled a " + str(roll))
else:
  print("Incorrect! They rolled a " + str(roll))
