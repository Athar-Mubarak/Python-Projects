#Dice roll simulator
""""
Key Concepts Used
import random: This line brings in Python's built-in random module,
which contains functions for generating random values.

random.randint(a, b): This is the core function for this project.
It generates a random integer N such that a≤N≤b (both endpoints are inclusive).
We use random.randint(1, 6) to perfectly simulate a standard six-sided die.

while Loop: This creates the main game loop, allowing the user to roll the dice
multiple times without restarting the program.

input(): This function is used to prompt the user and capture their response
to the "roll again" question.

String Method (.lower()): Using roll_again.lower() ensures that the user's input
is converted to lowercase ('yes', 'y'), making the program accept various
inputs like "Yes", "Y", or "yEs".

f-strings (f"You rolled a: {roll_dice()}"): This modern method makes it easy to embed variables and function calls directly inside a string for cleaner output.
"""
import random
def roll_dice():
    min_val = 1;
    max_val = 6

    roll = random.randint(min_val, max_val)
    return roll

roll_again = 'yes'

while roll_again.lower() in['yes', 'y']:
    print("Rolling the dice...")
    print(f"You rolled a: {roll_dice()} 🎲")

    roll_again = input("Do you want to roll the dice again?(yes/no): ")
print("Thanks for playing!")