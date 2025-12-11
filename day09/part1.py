from itertools import combinations

file = open("input.txt", "r")

points = []

for line in file.readlines():
    points.append([int(x) for x in line.strip().split(",")])

area = 0
for (a_x, a_y), (b_x, b_y) in combinations(points, 2):
    area = max(area, (abs(b_x - a_x) + 1) * (abs(b_y - a_y) + 1))

print(area)
