import random

secret_number = random.randint(1, 100)
max_attempts = 7

print(f"Guess the number (1-100). You have {max_attempts} attempts.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempt} attempts.")
        break
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")