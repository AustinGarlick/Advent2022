file = open("./Day4/input.txt", "r")

data = file.read()

data = data.split("\n")

# PART 1: Find the number of elves that are a subset of another elf's numbers

count = 0

for pair in data:
    pair = pair.split(",")

    # each elf is a range of numbers ie) 1-3
    elf1 = pair[0]
    elf2 = pair[1]

    elf1_obj = {"min": int(elf1.split("-")[0]), "max": int(elf1.split("-")[1])}

    elf2_obj = {"min": int(elf2.split("-")[0]), "max": int(elf2.split("-")[1])}

    # Check if one of the elves is a subset of the other
    if elf1_obj["min"] >= elf2_obj["min"] and elf1_obj["max"] <= elf2_obj["max"]:
        # print("Elf 1 is a subset of elf 2")
        count += 1
    elif elf2_obj["min"] >= elf1_obj["min"] and elf2_obj["max"] <= elf1_obj["max"]:
        # print("Elf 2 is a subset of elf 1")
        count += 1
    else:
        # print("No subset")
        pass


print(count)


# PART 2: Find the number of elves that are a overlap at all

count = 0

for pair in data:
    pair = pair.split(",")

    # each elf is a range of numbers ie) 1-3
    elf1 = pair[0]
    elf2 = pair[1]

    elf1_obj = {"min": int(elf1.split("-")[0]), "max": int(elf1.split("-")[1])}

    elf2_obj = {"min": int(elf2.split("-")[0]), "max": int(elf2.split("-")[1])}

    # Check if one of the elves overlaps with the other
    if elf1_obj["min"] <= elf2_obj["min"] and elf1_obj["max"] >= elf2_obj["min"]:
        # print("Elf 1 overlaps with elf 2")
        count += 1
    elif elf2_obj["min"] <= elf1_obj["min"] and elf2_obj["max"] >= elf1_obj["min"]:
        # print("Elf 2 overlaps with elf 1")
        count += 1
    else:
        # print("No overlap")
        pass

print(count)
