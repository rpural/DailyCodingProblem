#! /usr/bin/env python3

'''
    The user thinks of a number between 0 and 100. The program tries to 
    guess what the number is. The user supplies clues in the form of "higher"
    or "lower".
'''

high = 100
low = 0

print("Let's play a guessing game!")
print("You think of a number between 0 and 100. I'll make a guess, and")
print("you tell me if my guess is higher or lower than your number.")
print("If I take more than 7 guesses, you win! If I get it in 7 or less...")
print("\nFor each guess, your response should be '<', '=', or '>', for")
print("lower, correct, or higher.")
_ = input("\nThink of your number and then press return:")

guesses = 0

while True:
    mid = (high - low) // 2 + low - 1
    if mid < low:
        mid = low
    elif mid > high:
        mid = high

    if guesses >= 7:
        print("That was 7 guesses; You Win!")
        break

    guesses += 1
    guess = input(f"My guess:  {mid}.  Enter your response: ")
    if guess == "=":
        print(f"I win in {guesses} guesses!")
        break


    if guess == "<":
        high = mid - 1
        continue
    if guess == ">":
        low = mid + 1
        continue
