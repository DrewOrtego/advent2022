from re import search
from string import ascii_uppercase

file_name = 'input.txt'

def get_crates():
    """ 
    Build data structure for the stacks of crates
    ex: {1: ['N', 'Z'], 2: ['D', 'C', 'M'], 3: ['P']}
    """
    crates = {}
    with open(file_name, 'r') as file_data:
        for line in file_data.readlines():
            if line != '':
                for e, c in enumerate(line):  # e counts the char position
                    if c in ascii_uppercase:
                        if (e%4)+(e//4) not in crates:
                            crates.setdefault((e%4)+(e//4), list())
                        crates[(e%4)+(e//4)].append(c)
            else:
                break
    return crates

def get_instructions():
    """
    Use Regex to get instructions on how to move crates
    ex: [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    """
    instructions = []
    exp = r'move ([0-9]+) from ([0-9]+) to ([0-9]+)'

    with open(file_name, 'r') as file_data:
        for line in file_data.readlines():
            result = search(exp, line.strip())
            if result:
                instructions.append([int(g) for g in result.groups()])

    return instructions

def move_crates():
    for i in instructions:
        amount = i[0]
        source = i[1]
        destination = i[2]

        for r in range(amount-1, -1, -1):
            if crates[source]:
                crates[destination].insert(0, crates[source].pop(r))

def print_top_crates():
    message = ''
    for n in range(1,len(crates)+1):
        if crates[n]:
            message += crates[n][0]
    print(message)

if __name__ == "__main__":
    crates = get_crates()
    instructions = get_instructions()
    move_crates()
    print_top_crates()
