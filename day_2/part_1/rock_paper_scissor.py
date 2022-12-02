outcome = {
    # win
    'A Y': 8, 
    'B Z': 9,
    'C X': 7,

    # loss
    'A Z': 3,
    'B X': 1,
    'C Y': 2,

    # draw
    'A X': 4,
    'B Y': 5,
    'C Z': 6,
}

total_score = 0

with open(r'input.txt', 'r') as file_data:
    for line in file_data.readlines():
        total_score += outcome[line.strip()]

print(total_score)