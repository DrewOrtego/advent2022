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

sums = sorted(sums, reverse=True)
max_calories = sum(sums[:3])

print(max_calories)