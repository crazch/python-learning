"""
  Guess the Number Game
  - Generates a random number (1-100).
  - User guesses with high/low hints.
  Usage: Run `python random_number_guess.py`
  """

import random

target = random.randint(1, 100)

while True:
  try:
    guess = int(input("Enter Number(1-100): "))
  except ValueError:
    print("Invalid!")
    continue
  
  if guess > target:
    print("Too High!")
  elif guess < target:
    print("Too Low!")
  else:
    print("You Guessed it in!")