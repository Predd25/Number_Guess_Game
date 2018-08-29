#This program has the Number Guess dice game with it

from random import randint #makes the dice rolls random
from time import sleep #simulates dice rolls

def get_user_guess():
  guess = int(input("What is your guess for the dice rolled?: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("uhhhh that's not right, next" % guess)
  else:
    print("Rolling...")
    sleep(2)
    print("Your first roll results: %d" % first_roll)
    sleep(1)
    print("Your second roll results: %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("Your total roll is: %d" % total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You won!")
    else:
      print("You lose")

roll_dice(6)
