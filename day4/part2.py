total = 0

file = open("input.txt", "r")

grid = []
for line in file.readlines():
    grid.append(list(line.strip()))

changed = True

while changed:
    to_remove = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                count = 0

                for diffs in [
                    [-1, -1],
                    [-1, 0],
                    [-1, 1],
                    [0, -1],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                ]:
                    row_diff = row + diffs[0]
                    col_diff = col + diffs[1]

                    if 0 <= row_diff < len(grid) and 0 <= col_diff < len(grid[0]):
                        if grid[row_diff][col_diff] == "@":
                            count += 1

                if count < 4:
                    total += 1

                    to_remove.append((row, col))

    if to_remove == []:
        changed = False
    else:
        for row, col in to_remove:
            grid[row][col] = "."


print(total)
