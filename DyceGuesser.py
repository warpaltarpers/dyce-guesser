"""
Rolls a pair of dice and asks the users to guess the sum

Author: Maxwell Walters
"""

from random import randint
from time import sleep

def play():
    sides = int(input("How many sides will the dice have? "))
    roll_dice(sides)

def get_user_guess():
  guess = int(input("What is your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value of the dice rolls combined is %d" % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print("Your guess of %d is higher than the maximum value of %d" % (guess, max_val))
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d" % (first_roll))
    sleep(1)
    print("The second roll is %d" % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("The total is %d" % (total_roll))
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You've won! Congratulations!")
    else:
      print("Sorry, that isn't correct.")

play()
