file = open("input.txt", "r")


shapes = []

curr = []

fits = 0
for line in file.readlines():
    if "x" in line:
        line = line.strip().split(": ")

        dimensions = [int(x) for x in line[0].split("x")]
        needed = [int(x) for x in line[1].split()]

        total = sum(needed)

        boxes = (dimensions[0] // 3) * (dimensions[1] // 3)

        if boxes >= total:
            fits += 1

print(fits)
