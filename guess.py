import random
def game_start():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        num_of_guesses = 10
    elif level == "hard":
        num_of_guesses = 5
    else:
        print("invalid input")
        return
# # rule 1 with game_over variable
#     game_over = False
#     while not game_over:
#         print(f"You have {num_of_guesses} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#
#         if guess == number:
#             print(f"You got it! The answer was {number}")
#             return
#         elif guess > number:
#             print(f"Too high.\nGuess again.")
#         else:
#             print(f"Too low.\nGuess again.")
#
#         num_of_guesses -= 1
#         if num_of_guesses == 0:
#             game_over = True
#             print(f"You've run out of guesses. The number was {number}")
#
# game_start()

# rule 2 more direct approach
    while num_of_guesses > 0:
        print(f"\nYou have {num_of_guesses} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess > number:
            print(f"Too high.\nGuess again.")
        else:
            print(f"Too low.\nGuess again.")

        num_of_guesses -= 1
        if num_of_guesses == 0:
            print(f"You've run out of guesses. The number was {number}")

game_start()