import random

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You guessed one of the magic numbers!")
        return True
    else:
        print("You didn't guess one of the magic numbers")
        return False

magic_numbers = [random.randint(0,9), random.randint(0,9)]
chances = 3

for attempt in range(chances):
    print("This is attempt: {}".format(attempt))
    if ask_user_and_check_number():
        break

print("magic numbers were: {}".format(magic_numbers))