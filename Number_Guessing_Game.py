import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
