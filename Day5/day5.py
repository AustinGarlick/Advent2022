# file = open("/Users/austingarlick/Documents/GitHub/Advent2022/Day5/input_stacks.txt", "r")

# data = file.read()

# data = data.split("\n")

# # Create 9 queues
# queues = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

# # remove last element of data because its the row number names
# data.pop()

# # Set up queues based on data
# for line in reversed(data):
#     line = line.split(" ")

#     row = 1
#     index = 0
#     for i in range(0, 9):
#         item = line[index]
#         if item != "":
#             letter = item.replace("[", "")
#             letter = letter.replace("]", "")
#             queues[row].append(letter)
#             index += 1
#         else:
#             # Skip 4 empty spaces
#             index += 4
#         row += 1


# file = open("/Users/austingarlick/Documents/GitHub/Advent2022/Day5/input.txt", "r")

# data = file.read()

# data = data.split("\n")

# for move in data:
#     move = move.split(" ")

#     num_to_move = int(move[1])
#     from_stack = int(move[3])
#     to_stack = int(move[-1])

#     for i in range(0, num_to_move):
#         queues[to_stack].append(queues[from_stack].pop())

# # Create one string of top values of each stack

# final_string = ""
# for queue in queues.values():
#     final_string += queue[-1]

# print(final_string)


# PART 2: Mover now moves stacks at a time instead


file = open("/Users/austingarlick/Documents/GitHub/Advent2022/Day5/input_stacks.txt", "r")

data = file.read()

data = data.split("\n")

# Create 9 queues
queues = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

# remove last element of data because its the row number names
data.pop()

# Set up queues based on data
for line in reversed(data):
    line = line.split(" ")

    row = 1
    index = 0
    for i in range(0, 9):
        item = line[index]
        if item != "":
            letter = item.replace("[", "")
            letter = letter.replace("]", "")
            queues[row].append(letter)
            index += 1
        else:
            # Skip 4 empty spaces
            index += 4
        row += 1


file = open("/Users/austingarlick/Documents/GitHub/Advent2022/Day5/input.txt", "r")

data = file.read()

data = data.split("\n")

for move in data:
    move = move.split(" ")

    num_to_move = int(move[1])
    from_stack = int(move[3])
    to_stack = int(move[-1])

    # Move the last num_to_move stacks to the to_stack
    queues[to_stack].extend(queues[from_stack][-num_to_move:])
    queues[from_stack] = queues[from_stack][:-num_to_move]

# Create one string of top values of each stack

final_string = ""
for queue in queues.values():
    final_string += queue[-1]

print(final_string)
