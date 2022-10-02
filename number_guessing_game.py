import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
pc = random.randint(1, 100)
difficulty = input('Choose a difficulty: type "easy" or "hard": ')

def easy_mode():
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == pc:
            print(f"You got it! The answer was {pc}!")
            break
        elif guess < pc and guess > 0:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
        elif guess > pc and guess < 101:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
        else:
            print("You got out of range, try again!")


def hard_mode():
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == pc:
            print(f"You got it! The answer was {pc}!")
            break
        elif guess < pc and guess > 0:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
        elif guess > pc and guess < 101:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
        else:
            print("You got out of range, try again!")


repeat = True
while repeat:
    if difficulty == "easy":
        easy_mode()
        repeat = False
    elif difficulty == "hard":
        hard_mode()
        repeat = False
    else:
        print("Wrong! Type again!")
        difficulty = input('Choose a difficulty: type "easy" or "hard": ')
