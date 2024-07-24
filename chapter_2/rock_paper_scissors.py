"""
My recreation of the program Rock, Paper, Scissors based on output from the book Automate the boring stuff with python
"""

import random, sys




print(f"ROCK, PAPER, SCISSORS")



def main():
    wins = 0
    losses = 0
    ties = 0
    while True:
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")
        print(f"Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

        move = input("> ")

        comp_move = get_random_move()

        if move == "q":
            print("Thanks for the game dude!")
            break

        print(f"{move} versus...\n {comp_move}")

        if move == comp_move:
            print(f"It is a tie!")
            ties += 1
        elif move == "r" and comp_move == "p":
            print(f"You lose!")
            losses += 1
        elif move == "r" and comp_move == "s":
            print(f"You win!")
            wins += 1
        elif move == "p" and comp_move == "r":
            print(f"You win!")
            wins += 1
        elif move == "p" and comp_move == "s":
            print("You lose!")
            losses += 1
        elif move == "s" and comp_move == "p":
            print("You win!")
            wins += 1
        elif move == "s" and comp_move == "r":
            print("You lose!")
            losses += 1
        else:
            print("Wrong input\n")
    




def get_random_move():
    random_number = random.randint(1,3)
    
    # translate numbers to game moves
    if random_number == 1:
        return "p"
    elif random_number == 2:
        return "s"
    elif random_number == 3:
        return "r"
    else:
        return "Wrong "
    

if __name__ == '__main__':
    main()

