file = open("~/Advent2022/Day3/input.txt", "r")

data = file.read()


# Create a list of all the items in the input file by splitting on newlines
lists = data.split("\n")


score = 0

for item in lists:

    # Split item string into two parts of equal length

    # Get the first half of the item string
    first_half = item[: len(item) // 2]

    # Get the second half of the item string
    second_half = item[len(item) // 2 :]

    # find the shared character between the two halves
    for char in first_half:
        if char in second_half:
            shared_char = char
            break

    # Lowercase item types a through z have priorities 1 through 26
    # Uppercase item types A through Z have priorities 27 through 52
    # Get the priority of the shared character
    if shared_char.islower():
        shared_char_priority = ord(shared_char) - 96
    else:
        shared_char_priority = ord(shared_char) - 38

    score += shared_char_priority


# PART 2

score = 0

# Iterate through the list of items in groups of 3
for i in range(0, len(lists), 3):

    # Get the first item in the group
    first_item = lists[i]

    # Get the second item in the group
    second_item = lists[i + 1]

    # Get the third item in the group
    third_item = lists[i + 2]

    # Find the shared character between the first, second, and third items
    for char in first_item:
        if char in second_item and char in third_item:
            shared_char = char
            break

    if shared_char.islower():
        shared_char_priority = ord(shared_char) - 96
    else:
        shared_char_priority = ord(shared_char) - 38

    score += shared_char_priority
