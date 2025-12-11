total = 0

file = open("input.txt", "r")

grid = []
for line in file.readlines():
    grid.append(list(line.strip()))

changed = True

while changed:
    changed = False
    to_remove = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                count = 0

                for row_diff, col_diff in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                ]:
                    new_row = row + row_diff
                    new_col = col + col_diff

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == "@":
                            count += 1

                if count < 4:
                    total += 1
                    grid[row][col] = "."
                    changed = True


print(total)
