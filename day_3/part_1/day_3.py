from string import ascii_letters

with open(r'input.txt', 'r') as file_data:
    sum_letters = 0

    for line in file_data.readlines():
        half_len = len(line)//2

        line_left = line.strip()[:half_len]
        line_right = line.strip()[half_len:]

        unique_left = list(set(line_left))
        unique_right = list(set(line_right))

        for c in unique_left:
            if c in unique_right:
                sum_letters += ascii_letters.index(c) + 1
                break

print(sum_letters)
