import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    for _ in range(rounds):
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "win" in result:
            player_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")
    
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    play_game()
