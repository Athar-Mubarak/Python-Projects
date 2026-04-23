import random
target = random.randint(1,100)

while True:
    userchoice = input("Guess a number between 1 and 100 or Quit : ")
    if userchoice == "Quit":
        break
    userchoice = int(userchoice)
    if userchoice == target:
        print("Correct!")
    elif userchoice < target:
        print("Your guess is too low!")
    else :
        print("Your guess is too high!")

print("Thank you for playing...")


