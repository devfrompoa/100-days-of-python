with open("Input/Letters/starting_letter.txt", "r") as f:
    letter = f.readlines()

with open("Input/Names/invited_names.txt", "r") as f2:
    names = f2.readlines()

first_line = letter[0]

for name in names:
    new_name = name.strip("\n")
    new_first_line = first_line.replace("[name]", new_name)
    new_file = f"Output/ReadyToSend/letter_for_{new_name}.txt"
    with open(new_file, "w") as f3:
        f3.write(new_first_line)
        for letter_line in letter[1:]:
            f3.write(letter_line)
