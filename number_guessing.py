import random

computer_choice = random.randint(1, 10)

trials = 0

while trials <= 10:
    user_choice = int(input("Kindly make a choice between 1 and 10: "))
    if user_choice == computer_choice:
        print("Voilla😍")
        break
    else:
        print("You 🤣")
        
