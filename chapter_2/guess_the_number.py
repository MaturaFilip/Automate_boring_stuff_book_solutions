"""This is an attempt to recreate short program Guess the Number from the book Automate boring stuff

- Ask player to guess the number between 1 and 20
- Player should have 10 guesses
- Tell player if the guess was low or high after each round
"""

import random


MAX_ROUNDS = 10

def main():
    print(f"I am thinking of a number between 1 and 20.")
    while True:
        print("Guess the number")
        num_guesses = 1
        while num_guesses <= MAX_ROUNDS:

            print(f"round: {num_guesses}")
            guess = int(input())

            if guess < 1 or guess > 20:
                print('Wrong input!')
                break

            random_number = get_random_number()
            get_comparison(guess, random_number)
            num_guesses += 1

            if guess == random_number:
                break

            if num_guesses > MAX_ROUNDS:
                print(f"You are out of guesses")
                print(f"The correct answer was number {random_number}")


        print(f"Wanna play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break



def get_random_number():
    random_number = random.randint(1,20)
    return random_number

def get_comparison(guess, random_number):
    if guess == random_number:
        print('Correct!')
    elif guess > random_number:
        print('Your guess is too high.')
    elif guess < random_number:
        print('Your guess is too low.')
    else:
        print('Wrong input')


if __name__ == '__main__':
    main()