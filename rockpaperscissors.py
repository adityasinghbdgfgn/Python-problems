import random
def get_choices():
    player_choices = input("enter choice: rock paper or scissors: ")
    choices = ["rock", "paper", "scissors"]
    computer_choices = random.choice(choices)
    options = {"player": player_choices, "computer": computer_choices}
    return options

def check_win(player, computer):
    if player==computer:
        print ("tie")
    elif player=="rock":
        if computer=="paper":
            print("player wins")
        else: print ("computer wins")
    elif player == "paper":
        if computer=="rock": print("player wins")
        else: print ("computer wins")
    elif player=="scissor":
        if computer=="rock": print("computer wins")
        else: print("player wins")
    return


inputs = get_choices()
result = check_win(inputs["player"], inputs["computer"])
