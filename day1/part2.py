count = 0

dial = 50

file = open("input.txt", "r")


for line in file.readlines():
    line = line.strip()

    turns = int(line[1:])

    for i in range(turns):
        if line[0] == "L":
            dial -= 1
        else:
            dial += 1

        if dial == 0:
            count += 1
        elif dial == -1:
            dial = 99
        elif dial == 100:
            dial = 0
            count += 1


print(count)
