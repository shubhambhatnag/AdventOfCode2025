from functools import lru_cache
from tokenize import Triple

file = open("input.txt", "r")


graph = {}
for line in file.readlines():
    line = line.strip().split(": ")
    graph[line[0]] = line[1].split()

stack = [("svr", tuple())]

REQ1 = "fft"
REQ2 = "dac"


@lru_cache(None)
def count_paths(node, fft, dac):
    if node == "out":
        if fft and dac:
            return 1
        else:
            return 0

    if node == "fft":
        fft = True
    if node == "dac":
        dac = True
    return sum(count_paths(n, fft, dac) for n in graph[node])


print(count_paths("svr", False, False))
