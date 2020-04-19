#! /usr/bin/env python3

''' The 21 stone game:

    Starting with 21 stones, each of two players may remove
    1 or 2 stones, alternating until one player gets the last
    stone and wins.
'''

import random

print("21 Stones")
print("=========")
print("""\nThere are currently 21 stones in the row. On each turn,
         you may remove 1 or 2 stones. The person who removes the
         last stone wins.\n""")

num_stones = 21

while True:
    print(num_stones * "# ")
    while True:
        # Get the player's move:
        try:
            player_move = int(input("How many stones would you like to remove?"))
        except ValueError:
            print("That wasn't a valid number; try again.")
            continue
        if not (1 <= player_move <= 2):
            print("That wasn't a 1 or a 2; try again.")
            continue
        if player_move > num_stones:
            print(f"There aren't {player_move} stones to take; try again.")
            continue
        break

    num_stones -= player_move

    if num_stones == 0:
        print("You win!")
        break

    # Generate the computer's move:

    '''
    # First pass: create a nieve move (randomly picking 1 or 2)
    print(num_stones * "# ")
    computer_move = random.randint(1, 2)
    if computer_move > num_stones:
        computer_move = num_stones
    '''

    # Second pass: try to keep the total count odd
    if num_stones < 3:
        computer_move = num_stones
    elif num_stones % 2 == 0: # otherwise, try to keep the count odd
        computer_move = 1
    else:
        computer_move = 2

    num_stones -= computer_move
    print(f"Computer removed {computer_move} stones.")

    if num_stones == 0:
        print("The computer wins!")
        break
