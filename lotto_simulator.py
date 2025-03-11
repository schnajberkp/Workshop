import random

def get_user_numbers():
    selected_numbers = []

    while len(selected_numbers) < 6:
        try:
            number = int(input(f"Enter number {len(selected_numbers) +1}/6 (1-49):  "))

            if number < 1 or number > 49:
                print("Number must be between 1 and 49")
            elif number in selected_numbers:
                print("Number already exists")
            else:
                selected_numbers.append(number)
        except ValueError:
            print("Number must be an integer")
    return sorted(selected_numbers)

user_numbers = get_user_numbers()
lottery_numbers = random.sample(range(1, 50),6)

matches = set (user_numbers) & set(lottery_numbers)

print("Your numbers:", user_numbers)
print("Lottery numbers:", lottery_numbers)
if matches:
    print(f"You matched {len(matches)} numbers: {sorted(matches)}")
else:
    print("No matches, better luck next time!")