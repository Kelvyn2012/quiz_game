import random

max_range = 20
min_range = 1
guess_no = 0
answer = random.randint(min_range, max_range)

print("............Guessing Game.................")
print()

while True:
    guess = input(f"Guess a number between {min_range} and {max_range}: ")

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)
    guess_no += 1

    if guess > max_range or guess < min_range:
        print(
            f"{guess} is out of range. Please enter a number between {min_range} and {max_range}."
        )
        continue

    if guess > answer:
        print(f"{guess} is higher than the lucky number, TRY AGAIN.")

    elif guess < answer:
        print(f"{guess} is lower than the lucky number, TRY AGAIN.")

    else:
        print(f"🎉 CORRECT! The lucky number is {guess}.")
        break

print(".............................")
print(f"You got the lucky number in {guess_no} guesses.")
