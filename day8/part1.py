import math
from collections import defaultdict
from itertools import combinations

file = open("input.txt", "r")
connections = 1000

boxes = []

for line in file.readlines():
    boxes.append([int(x) for x in line.strip().split(",")])

distances = []
for a, b in combinations(boxes, 2):
    d = math.dist(a, b)
    distances.append((d, tuple(a), tuple(b)))

distances.sort()

circuits = []
for distance in distances[:connections]:
    exists = False
    circuit1 = set()
    circuit2 = set()
    to_remove = set()
    for circuit in range(len(circuits)):
        if distance[1] in circuits[circuit]:
            circuit1 = circuits[circuit]
            to_remove.add(circuit)
        if distance[2] in circuits[circuit]:
            circuit2 = circuits[circuit]
            to_remove.add(circuit)

    if circuit1 == set() and circuit2 == set():
        circuits.append(set([distance[1], distance[2]]))
    else:
        for i in sorted(to_remove, reverse=True):
            circuits.pop(i)

        circuits.append(circuit1.union(circuit2).union(set([distance[1], distance[2]])))


sizes = [len(circuit) for circuit in circuits]

product = 1
for size in sorted(sizes, reverse=True)[:3]:
    product *= size

print(product)
