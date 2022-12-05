with open(r'input.txt', 'r') as file_data:
    fully_contained_pairs = 0

    for line in file_data.readlines():
        # ex: "2-4,6-8"
        range_one, range_two = line.strip().split(',')

        # ex: ["2","4"],["6","8"]
        range_one = list(range_one.split('-'))
        range_two = list(range_two.split('-'))

        # ex: [2,4],[6,8]
        range_one = [int(n) for n in range_one]
        range_two = [int(n) for n in range_two]

        # ex: [2,3,4],[6,7,8]
        range_one = list(range(range_one[0], range_one[1]+1))
        range_two = list(range(range_two[0], range_two[1]+1))

        if range_one[0] in range_two or range_one[-1:] in range_two:
            fully_contained_pairs += 1
        elif range_two[0] in range_one or range_two[-1:] in range_one:
            fully_contained_pairs += 1
        else:
            pass

print(fully_contained_pairs)