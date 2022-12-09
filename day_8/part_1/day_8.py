with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

forest = {}

# Build coordinates/values: {'r0c0': 1, 'r0c1': 2, 'r1c0': 3, 'r1c1': 4}
for r, row in enumerate(lines):
    for c, col in enumerate(row):
        forest.update({f'r{r}c{c}': int(col)})

rows = len(lines)
columns = len(lines[0])
visibility_map = [['v' for _ in range(rows)] for _ in range(columns)]  # [[0,0], [0,0]]

for r in range(rows):
    for c in range(columns):
        tree = forest[f'r{r}c{c}']

        # Check whether the tree is on an edge
        if r == 0 or r == rows or c == 0 or c == columns:
            continue
        
        # check left for visibilty
        if any(map(lambda x: x >= tree, [forest[f"r{r}c{col}"] for col in range(c)])):
            visibility_map[r][c] = 'h'
        else:
            visibility_map[r][c] = 'v'
            continue

        # check right
        if any(map(lambda x: x >= tree, [forest[f"r{r}c{col}"] for col in range(c+1,columns)])):
            visibility_map[r][c] = 'h'
        else:
            visibility_map[r][c] = 'v'
            continue

        # check up
        if any(map(lambda x: x >= tree, [forest[f"r{row}c{c}"] for row in range(r)])):
            visibility_map[r][c] = 'h'
        else:
            visibility_map[r][c] = 'v'
            continue

        # check down
        if any(map(lambda x: x >= tree, [forest[f"r{row}c{c}"] for row in range(r+1,rows)])):
            visibility_map[r][c] = 'h'
        else:
            visibility_map[r][c] = 'v'
            continue

print(sum([v.count('v') for v in visibility_map]))