sums = []
value = 0

with open(r'input.txt', 'r') as file_data:
    for line in file_data.readlines():
        if line == '\n':
            sums.append(value)
            value = 0
        else:
            value += int(line.strip())
    sums.append(value)  # get the last value stored before readline finished

max_calories = max(sums)
alpha_elf = sums.index(max_calories) + 1

print(f"Elf #{alpha_elf} has brought {max_calories} calories!")
