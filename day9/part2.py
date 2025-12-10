from itertools import combinations

file = open("input.txt", "r")

points = []

for line in file.readlines():
    points.append([int(x) for x in line.strip().split(",")])
points.append(points[0])
on_line = set()


for point in range(len(points) - 1):
    (x1, y1), (x2, y2) = points[point], points[point + 1]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            on_line.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            on_line.add((x, y1))

points.pop(-1)

sorted_pairs = sorted(
    combinations(points, 2),
    key=lambda pair: abs(pair[1][0] - pair[0][0]) * abs(pair[1][1] - pair[0][1]),
    reverse=True,
)


for (a_x, a_y), (b_x, b_y) in sorted_pairs:
    valid = True
    area = (abs(b_x - a_x) + 1) * (abs(b_y - a_y) + 1)

    for x, y in on_line:
        if min(a_x, b_x) < x < max(a_x, b_x) and min(a_y, b_y) < y < max(a_y, b_y):
            valid = False
            break

    if valid:
        print(area)
        break
