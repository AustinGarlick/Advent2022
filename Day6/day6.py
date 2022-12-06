file = open("./Day6/input.txt", "r")

data = file.read()


count = 0
last_4_chars = []
for char in data:

    last_4_chars.append(char)
    if len(last_4_chars) > 4:
        last_4_chars.pop(0)
    count += 1

    # Check if each char in last_4_chars is a different char
    if len(set(last_4_chars)) == 4:
        print(count)
        break

# Part 2  Find first 14 chars that are all different

count = 0
last_14_chars = []
for char in data:

    last_14_chars.append(char)
    if len(last_14_chars) > 14:
        last_14_chars.pop(0)
    count += 1

    # Check if each char in last_14_chars is a different char
    if len(set(last_14_chars)) == 14:
        print(count)
        break
