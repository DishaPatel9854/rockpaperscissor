import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    result = determine_winner(player_choice, computer_choice)

    return f"Computer chose {computer_choice}. {result}"


player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

if player_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    game_result = play_game(player_choice)
    print(game_result)

