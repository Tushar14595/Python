# NUMBER GUESSING NUMBER

# Make a variable, like winning number and assign any number to it. 
# Ask user to guess a number 
# if user gussed properly then print "you win"!!!
# if user not gussed properly then :
    # 1 - if user guessed lower number then print "too low "
    # 2 - if user guessed higher number then print "too high"

# Program to generate a random number between 0 and 9

# importing the random module
import random
# winning_number = random.randint(10,100)
winning_number = 19 
# guess = 19
number = int(input("Guess the number between 10-100:- "))
# game_over = False
# while not game_over:
if number == winning_number:
    print(f"You entered  {number} You won!!")
    # game_over = True
else:
    if number < winning_number:
     print("too low")
    else:
     print("too high ")
# guess += 1
# number = int("Guess again:-")