import random

choices = ("rock","scissors","paper")

playing = True
while playing:

    player = input("\nEnter Your Weapon: ").lower()
    computer = random.choice(choices) 

    while player not in choices :
        print(f"TERi MKC yeh {player} kya h?")
        player = input("Enter Your Weapon: ").lower()

    print(f"Player : {player}")
    print(f"computer:{computer}")

    if computer == "rock" and player == "paper":
        print("DATTEBAYO !! You Win!")
    elif computer == "scissors" and player == "rock":
        print("DATTEBAYO !! You Win!")
    elif computer == "paper" and player == "scissors":
        print("DATTEBAYO !! You Win!")
    elif computer == player :
        print("tie match")
    else :
        print("You are NOOB computer has win the game")

    play_again = input("play again y/n : ").lower()
    if play_again !="y" :
        playing = False
print("THanks For Playing !")
    

