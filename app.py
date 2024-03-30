# Imports
import random

# List of valid moves:
moves = ['rock', 'paper', 'scissors']
score = {'user': 0, 'computer': 0}

# Function to take user input  
def user_input():
    print("\n")
    user_move = input("Enter your move: ")
    user_move = user_move.lower()
    if user_move in moves:
        return user_move
    elif user_move == 'quit':
        return 'quit'
    else:
        print("Invalid move. Please enter rock, paper, or scissors.")
        return user_input()
    
# Function to generate computer move
def computer_move():
    return random.choice(moves)

# Function to determine winner
def determine_winner(user, computer):
    print("\n")
    if user == computer:
        return "It's a tie!"
    elif user == 'rock' and computer == 'scissors':
        score['user'] += 1
        return "You win!"
    elif user == 'scissors' and computer == 'paper':
        score['user'] += 1
        return "You win!"
    elif user == 'paper' and computer == 'rock':
        score['user'] += 1
        return "You win!"
    else:
        score['computer'] += 1
        return "You lose!"
    
# Start game
def start_game():
    print("\n******\n")
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'quit' to exit the game on any prompt.")
    print("Otherwise enter rock, paper, or scissors.")
    print("Good luck!")
    
# End round
def end_round():
    game_end = False
    print("\n******\n")
    print(f"Current Score: User - {score['user']}, Computer - {score['computer']}")
    rematch = input("Type quit to end the game, otherwise you will keep playing!: ")
    if rematch == 'quit':
        game_end = True
        return game_end
    else:
        print("Next round!")
        return game_end

# End game
def end_game():
    print("\n******\n")
    print("Game Over!")
    print(f"Final Score: User - {score['user']}, Computer - {score['computer']}")
    if score['user'] > score['computer']:
        print("You win!")
    elif score['user'] < score['computer']:
        print("You lose!")
    else:
        print("It's a tie!")
        
# Main function
def main():
    start_game()
    game_end = False
    while not game_end:
        user = user_input()
        if user == 'quit':
            game_end = True
            break
        computer = computer_move()
        print(f"Computer's move: {computer}")
        print(determine_winner(user, computer))
        game_end = end_round()
    end_game()
    
# Run the game
if __name__ == '__main__':
    main()