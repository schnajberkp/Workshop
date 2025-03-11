def computer_guess():
    #Range of numbers
    low = 1
    high =1000
    attempts = 0

    print("I challenge you to think of a number between 1 and 1000, and I'll guess it")

    while True:
        #Middle of range
        guess = int((low + high) /2)
        attempts += 1
        print(f"My guess is {guess}")

        response = input("Enter 'Too small', 'Too big', or 'You win': ").strip().lower()

        if response == "too small":
            # Narrow search to higher half
            low = guess + 1
        elif response == "too big":
            # Narrow search to higher half
            high = guess - 1
        elif response == "you win":
            print(f"I won in {attempts} attempts")
            break # Exit the loop when number is found
        else:
            print("Invalid response, please enter 'Too small', 'Too big', or 'You win'")
computer_guess()