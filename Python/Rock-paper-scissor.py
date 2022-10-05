import random
from enum import IntEnum

class Chance(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Chance]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Chance(selection)
    return action

def computer_turn():
    selection = random.randint(0, len(Chance) - 1)
    action = Chance(selection)
    return action

def Choose_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Chance.Rock:
        if computer_action == Chance.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Chance.Paper:
        if computer_action == Chance.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Chance.Scissors:
        if computer_action == Chance.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Chance) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = computer_turn()
    Choose_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break