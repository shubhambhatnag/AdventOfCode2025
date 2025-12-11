file = open("input.txt", "r")


graph = {}
for line in file.readlines():
    line = line.strip().split(": ")
    graph[line[0]] = line[1].split()

stack = [("you", tuple())]

paths = []
while stack:
    curr, path = stack.pop()
    for neighbor in graph[curr]:
        current_path = list(path)
        if neighbor == "out":
            paths.append(tuple(list(current_path)))
        else:
            stack.append((neighbor, tuple(list(current_path) + [neighbor])))

print(len(paths))
