from functools import lru_cache

file = open("input.txt", "r")


graph = {}
for line in file.readlines():
    line = line.strip().split(": ")
    graph[line[0]] = line[1].split()


@lru_cache(None)
def count_paths(node, end):
    if node == end:
        return 1
    if node == "out":
        return 0
    return sum(count_paths(n, end) for n in graph[node])


print(count_paths("fft", "dac"))
