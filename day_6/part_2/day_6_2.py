file_name = 'input.txt'

with open(file_name, 'r') as file_data:
    for line in file_data.readlines():
        for e, _ in enumerate(line):
            if e+14 > len(line):
                break
            elif len(list(set(line[e:e+14]))) == 14:
                print(e+14)
                break