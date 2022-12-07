file_name = 'input.txt'

with open(file_name, 'r') as file_data:
    for line in file_data.readlines():
        for e, _ in enumerate(line):
            if e+4 > len(line):
                break
            elif len(list(set(line[e:e+4]))) == 4:
                print(e+4)
                break