from random import randint

# Mapping for choices
choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

# Initialize scores
computerScore = 0
playerScore = 0

def game(playerScore, computerScore):
    print("Welcome to Rock, Paper, Scissors!\n")
    
    while True:
        try:
            # Get player choice
            playerChoice = int(input("Choose between Rock (0), Paper (1), or Scissors (2). Enter -1 to quit: "))
            if playerChoice == -1:
                print("Thanks for playing!")
                break
            if playerChoice not in [0, 1, 2]:
                print("Invalid choice. Please choose 0, 1, or 2.")
                continue
            
            # Generate computer choice
            computerChoice = randint(0, 2)

            print(f"\nYou chose: {choices[playerChoice]}")
            print(f"Computer chose: {choices[computerChoice]}\n")

            # Determine the winner
            if computerChoice == playerChoice:
                print("It's a tie!")
            elif (playerChoice == 0 and computerChoice == 2) or \
                 (playerChoice == 1 and computerChoice == 0) or \
                 (playerChoice == 2 and computerChoice == 1):
                print("You won this round!")
                playerScore += 1
            else:
                print("Computer won this round!")
                computerScore += 1

            # Display scores
            print(f"\nScores:\nYou: {playerScore}\nComputer: {computerScore}\n")
        
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, 2, or -1 to quit).")

    return playerScore, computerScore

if __name__ == "__main__":
    finalPlayerScore, finalComputerScore = game(playerScore, computerScore)
    print(f"\nFinal Scores:\nYou: {finalPlayerScore}\nComputer: {finalComputerScore}")
    print("Goodbye!")
