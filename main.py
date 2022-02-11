import random
from art import logo

print(logo)

turns_available = 0
game_over = 0

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

num_to_guess = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
if difficulty == 'hard':
    turns_available = 5
else:
    turns_available = 10

while game_over != 1:
    print(f"You have {turns_available} attempts remaining to guess the number.")
    player_guess = int(input("Enter a guess: "))

    if player_guess < num_to_guess:
        print("Too low.")
    elif player_guess > num_to_guess:
        print("Too high.")
    elif player_guess == num_to_guess:
        game_over = 1
        print(f"You win! The answer was: {num_to_guess}")

    turns_available -= 1
    if turns_available == 0:
        game_over = 1

if turns_available == 0 and game_over == 1:
    print("You have run out of guesses, you lose.")





