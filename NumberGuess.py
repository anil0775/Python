#This is a program that rolls a pair of dice and asks the user to guess #the sum. If the users guess is equal to the total value of the dice #roll, the user wins! Otherwise, the computer wins
from random import randint
from time import sleep
def get_user_guess():
 guess = int(raw_input("Enter your guess: "))
 return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_value = number_of_sides * 2
  print "Maximum possible value of the rolls is %d" + str(max_value)
  guess = get_user_guess()
  if guess > max_value:
    print "Invalid guess. Your guess exceeds maximum allowed value."
  else:
    print "Rollng..."
    sleep(2)
    print "First roll is %d" %(first_roll)
    sleep(1)
    print "Second roll is %d" %(second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total Roll is %d" %(total_roll)
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You have won!!!"
    else:
      print "You have lost! Please try again!"
roll_dice(6)