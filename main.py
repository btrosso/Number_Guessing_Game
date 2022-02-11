import random
from art import logo

print(logo)


def set_difficulty():
    """
    Function to set the difficulty of the game.
    :return int:
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if difficulty == 'hard':
        return 5
    else:
        return 10


def compare(p_guess, num):
    """
    Compares the player's guess to the randomly chosen number.
    :param p_guess:
    :param num:
    :return bool:
    """
    if p_guess < num:
        print("Too low.")
        return False
    elif p_guess > num:
        print("Too high.")
        return False
    elif p_guess == num:
        print(f"You win! The answer was: {num}")
        return True


def welcome_message():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")


def game():
    turns_available = set_difficulty()
    game_over = False

    welcome_message()

    num_to_guess = random.randint(1, 100)

    while game_over != 1:
        print(f"You have {turns_available} attempts remaining to guess the number.")
        player_guess = int(input("Enter a guess: "))

        game_over = compare(p_guess=player_guess, num=num_to_guess)

        turns_available -= 1

        if turns_available == 0:
            game_over = True

    if turns_available == 0 and game_over:
        print("You have run out of guesses, you lose.")


game()
