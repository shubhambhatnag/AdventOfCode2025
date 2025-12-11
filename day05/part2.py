total = 0

file = open("input.txt", "r")

fresh = 0

ranges = []
merged = []

for line in file.readlines():
    if line == "\n":
        ranges = sorted(ranges)
        merged = [ranges[0]]

        for start, end in ranges[1:]:
            last_start, last_end = merged[-1]

            if start <= last_end:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))

        for start, end in merged:
            fresh += end - start + 1
        break

    ranges.append([int(x) for x in line.strip().split("-")])

print(fresh)
