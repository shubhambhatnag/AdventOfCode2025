from functools import lru_cache

file = open("input.txt", "r")
grid = [list(line.strip()) for line in file.readlines()]

start = (None, None)
for row in range(len(grid)):
    if "S" in grid[row]:
        start = (row, grid[row].index("S"))

hit = set()


@lru_cache(maxsize=None)
def simulate_beam(row, col):
    for i in range(row + 1, len(grid)):
        if grid[i][col] == "^":
            # print("hit at ", (i, col))
            hit.add((i, col))
            return 1 + simulate_beam(i, col + 1) + simulate_beam(i, col - 1)

    return 0


print(len(hit))
