def menu():
    # ask player for numbers
    playerNumbers = get_player_numbers()
    # calculate numbers
    winning_numbers = create_lottery_numbers()
    # print out the winnings
    matched_numbers = playerNumbers.intersection(winning_numbers)
    print("Winning Numbers: {}".format(winning_numbers))
    print("matched numbers: {}".format(matched_numbers))
    if len(matched_numbers):
        print("You matched {} numbers: {}".format(len(matched_numbers), matched_numbers))
        print("You won ${} !".format(100 ** len(matched_numbers)))
    else:
        print("You didn't match any numbers!")

# lottery program from Udemy
def get_player_numbers():
    numbers_csv = input("Enter your 6 numbers separated by commas: ")
    # create a set of integers from the input
    integer_set = {int(i) for i in numbers_csv.split(',')}
    return integer_set

# calculate 6 unique random numbers between 1 and 20
# using a set to weed out duplicates
def create_lottery_numbers():
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        random_lotto = random.randint(1,20)
        lotto_numbers.add(random_lotto)

    return lotto_numbers

menu()
