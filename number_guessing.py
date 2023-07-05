from guizero import App, Text, TextBox, PushButton, Box
import random

app = App("Guess Game", bg="orange")

trials = 0
computer_choice = random.randint(1, 10)

def play():
    global trials
    trials += 1
    
    guess = int(choice_box.value)
    if guess < computer_choice:
        outcome.value = "Too low!!"

    elif guess > computer_choice:
        outcome.value = "Too high!!"
            
    else:
        outcome.value = "You rock! 😍"
    
    if trials >= 10:
        outcome.value = "Game Over! You ran out of trials."

def reset_game():
    global trials, computer_choice
    trials = 0
    computer_choice = random.randint(1, 10)
    outcome.value = ""
    choice_box.clear()
    choice_box.enable()

grid = Box(app, layout="grid")

title = Text(grid, text="Guess a number between 1 and 10", grid=[0, 0, 2, 1])
label = Text(grid, text="Your guess:", grid=[0, 1])

choice_box = TextBox(grid, width=5, grid=[1, 1])
choice_box.bg = "white"

check_button = PushButton(grid, play, text="Check", grid=[2, 1])
check_button.text_color = "white"
check_button.bg = "green"

outcome = Text(grid, text="", grid=[0, 2, 3, 1])
outcome.text_color = "white"

reset_button = PushButton(grid, reset_game, text="Reset", grid=[3, 1])
reset_button.bg = "Red"
reset_button.text_color = "white"

message = Text(grid, text="We have selected a random number between 1 and 10.", grid=[0, 3, 3, 1])
message = Text(grid, text="See if you can guess it in 10 turns or fewer.", grid=[0, 4, 4, 2])
message = Text(grid, text="We'll tell you if your guess was too high or too low.", grid=[0, 6, 5, 3])

app.display()
