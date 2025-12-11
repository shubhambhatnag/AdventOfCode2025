count = 0

dial = 50

file = open("input.txt", "r")


for line in file.readlines():
    line = line.strip()

    if dial == 0:
        count += 1

    if line[0] == "L":
        line = int(line[1:]) * -1
    else:
        line = int(line[1:])

    dial += line

    dial %= 100


print(count)
