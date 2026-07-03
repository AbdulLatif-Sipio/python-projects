import random

# Maps player's number input to the actual choice word
choices = {1: "rock", 2: "paper", 3: "scissor"}

# Get player's choice
player_ip = input(
    "Choose and write any one of these : "
    "\n 1-Rock       2-paper    3-scissor: "
    "\n"
)

try:
    # Cleaning up the extra spaces/capitalization
    player_ip = player_ip.strip().lower()

    if player_ip.isdigit(): # If Player typed a number
        
        player = choices[int(player_ip)]
    elif player_ip in choices.values(): # If Player typed a word
        
        player = player_ip
    else:
        #If entered something invalid (e.g. "banana", "5")
        raise ValueError("Invalid choice")

    # Computer randomly picks one of the three choice words
    computer_ip = random.choice(list(choices.values()))

    print("The computer chose " + computer_ip)

    # Two sets of winning combinations: one where computer wins, one where player wins
    computer_wins = [("rock", "scissor"), ("paper", "rock"), ("scissor", "paper")]
    player_wins = [("scissor", "rock"), ("rock", "paper"), ("paper", "scissor")]

    if computer_ip == player:
        print("It's a draw! Try again")
    elif (computer_ip, player) in computer_wins:
        print("The computer won!")
    elif (computer_ip, player) in player_wins:
        print("Congrats! You won..")

except ValueError:
    # Happens if player types something that isn't 1/2/3 or rock/paper/scissor
    print("Please enter 1, 2, 3, or rock/paper/scissor.")
except KeyError:
    # Happens if player types a number outside 1, 2, 3 (e.g. 5)
    print("Please choose only 1, 2, or 3.")