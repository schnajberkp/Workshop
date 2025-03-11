from random import randint
computer_draw = randint(1, 100)
print(computer_draw)
user_guess = None

while user_guess != computer_draw:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess < computer_draw:
            print("Too low.")
        elif user_guess > computer_draw:
            print("Too high.")
        elif user_guess == computer_draw:
            print("You guessed right!")
    except ValueError:
        print("It's not a valid number. Try again.")