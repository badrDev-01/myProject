import random


def guess_number():
    number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it!")
            break


if __name__ == "__main__":
    guess_number()