outcome = {
    # lose
    'A X': 3,
    'B X': 1,
    'C X': 2,

    # draw
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,

    # win
    'A Z': 8,
    'B Z': 9,
    'C Z': 7,
}

total_score = 0

with open(r'input.txt', 'r') as file_data:
    for line in file_data.readlines():
        total_score += outcome[line.strip()]

print(total_score)