total = 0

file = open("input.txt", "r")

fresh = 0

ranges = []
merged = []
switch = False
for line in file.readlines():
    if switch:
        num = int(line.strip())

        for start, end in merged:
            if start <= num <= end:
                fresh += 1
                break

    if line == "\n":
        ranges = sorted(ranges)
        merged = [ranges[0]]

        for start, end in ranges[1:]:
            last_start, last_end = merged[-1]

            if start <= last_end:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))

        switch = True
        continue

    ranges.append([int(x) for x in line.strip().split("-")])

print(fresh)
