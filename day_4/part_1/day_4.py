with open(r'input.txt', 'r') as file_data:
    fully_contained_pairs = 0

    for line in file_data.readlines():
        range_one, range_two = line.strip().split(',')
        range_one = list(range_one.split('-'))
        range_two = list(range_two.split('-'))


        if int(range_one[0]) <= int(range_two[0]) and int(range_one[1]) >= int(range_two[1]):
            fully_contained_pairs += 1
        elif int(range_one[0]) >= int(range_two[0]) and int(range_one[1]) <= int(range_two[1]):
            fully_contained_pairs += 1
        else:
            pass

print(fully_contained_pairs)