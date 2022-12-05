file = open("~/Advent2022/Day1/input.txt", "r")

data = file.read()


# split data on two new lines
lists = data.split("\n\n")

# split each list on new line
lists = [x.split("\n") for x in lists]

scores = []

for elf in lists:
    temp_sum = 0
    for number in elf:
        temp_sum += int(number)

    scores.append(temp_sum)


# sort scores
scores.sort()

# sum up top 3 scores
top_three = scores[-3:]

sum_score = 0
for score in top_three:
    sum_score += score
