from collections import deque

file = open("input.txt", "r")

total = 0

for line in file.readlines():
    line = line.strip().split()

    needed = tuple([0 if char == "." else 1 for char in line[0][1:-1]])
    buttons = []

    for button in line[1:-1]:
        button = [int(num) for num in button[1:-1].split(",")]
        buttons.append(button)

    queue = deque()

    start_state = tuple([0] * len(needed))
    queue.append((start_state, 0))
    visited = {start_state}

    while True:
        state, depth = queue.popleft()

        if state == needed:
            total += depth
            break

        for option in buttons:
            new_state = list(state)

            for light in option:
                new_state[light] ^= 1

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, depth + 1))

print(total)
