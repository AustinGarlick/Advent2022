file = open("./Day2/input.txt", "r")

data = file.read()


their_score = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

my_scores = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

# 0 for a loss
# 3 for a tie
# 6 for a win

# split data on new line
lists = data.split("\n")


my_total_score = 0

for game in lists:
    them = game[0]
    me = game[-1]

    # Calculate score for game and add to total
    # Rock beats scissors
    # Paper beats rock
    # Scissors beats paper
    if their_score[them] == my_scores[me]:
        my_total_score += 3
        my_total_score += my_scores[me]
    elif their_score[them] == 1 and my_scores[me] == 3:
        my_total_score += my_scores[me]
    elif their_score[them] == 2 and my_scores[me] == 1:
        my_total_score += my_scores[me]
    elif their_score[them] == 3 and my_scores[me] == 2:
        my_total_score += my_scores[me]
    else:
        my_total_score += 6
        my_total_score += my_scores[me]


print(my_total_score)


# PART 2

their_score = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}
my_scores = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

# X means to lose
# Y means to tie
# Z means to win

new_score = 0

for game in lists:
    them = game[0]
    outcome = game[-1]

    # Calculate score for game and add to total
    # Rock beats scissors
    # Paper beats rock
    # Scissors beats paper
    if outcome == "X":
        if their_score[them] == 1:
            new_score += my_scores["Z"]
        elif their_score[them] == 2:
            new_score += my_scores["X"]
        elif their_score[them] == 3:
            new_score += my_scores["Y"]
    elif outcome == "Y":
        if their_score[them] == 1:
            new_score += my_scores["X"]
        elif their_score[them] == 2:
            new_score += my_scores["Y"]
        elif their_score[them] == 3:
            new_score += my_scores["Z"]
        new_score += 3  # Add 3 for tie
    elif outcome == "Z":
        if their_score[them] == 1:
            new_score += my_scores["Y"]
        elif their_score[them] == 2:
            new_score += my_scores["Z"]
        elif their_score[them] == 3:
            new_score += my_scores["X"]
        new_score += 6  # Add 6 for win

print(new_score)
