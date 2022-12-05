from string import ascii_letters

with open(r'input.txt', 'r') as file_data:
    lines = file_data.readlines()

sum_letters = 0

groups = []
for e, line in enumerate(lines):
    if (e+1) % 3 != 0:
        groups.append(line)
    else:
        groups.append(line)
        unique_one, unique_two, unique_three = [list(set(line.strip())) for line in groups]

        for c in unique_one:
            if c in unique_two and c in unique_three:
                sum_letters += ascii_letters.index(c) + 1
                break

        groups = []

print(sum_letters)
