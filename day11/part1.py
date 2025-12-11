from functools import lru_cache

file = open("input.txt", "r")


graph = {}
for line in file.readlines():
    line = line.strip().split(": ")
    graph[line[0]] = line[1].split()


@lru_cache(None)
def count_paths(node):
    if node == "out":
        return 1
    return sum(count_paths(n) for n in graph[node])


print(count_paths("you"))
