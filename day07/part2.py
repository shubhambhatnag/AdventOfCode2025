file = open("input.txt", "r")
grid = [list(line.strip()) for line in file.readlines()]
output = [0] * len(grid[0])
for row in range(len(grid)):
    if "S" in grid[row]:
        output[grid[row].index("S")] = 1

for row in range(1, len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "^":
            output[col - 1] += output[col]
            output[col + 1] += output[col]
            output[col] = 0


print(sum(output))
