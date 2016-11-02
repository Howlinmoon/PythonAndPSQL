numbers = set()

numbers.add(3)

print(numbers)


lottery_values = {3, 5, 17, 6}
user_values = {3, 5, 11, 2}

matches = lottery_values.intersection(user_values)
print("set intersection: {}".format(matches))